'''
common functions for interacting with BigQuery within the dreams labs data ecosystem. all
functions are initiated through the BigQuery() class which contains credentials, project ids, and
other relevant metadata. 
'''
# pylint: disable=C0301

import datetime
import os
import logging
import json
from urllib.parse import urlencode
from pytz import utc
import pandas as pd
import aiohttp
import pandas_gbq
import google.auth
from google.api_core.exceptions import NotFound
from google.auth.transport.requests import AuthorizedSession
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.cloud import bigquery
from google.cloud import storage
from google.cloud import bigquery_storage
import gspread


class GoogleCloud:
    ''' 
    A class to interact with BigQuery. This class is designed
    to be used in the context of the Dreams project. It is not
    intended to be a general purpose BigQuery class.

    Params: 
        service_account_json (str): Path to the service account JSON file. if no value is input \
        the functions will default to using the path in the env var GOOGLE_APPLICATION_CREDENTIALS
    '''

    def __init__(
            self,
            service_account_json_path=None
        ):
        # load credentials using service account and scope
        if service_account_json_path is None:
            service_account_json_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        scopes=[
            "https://www.googleapis.com/auth/cloud-platform",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/bigquery",
            "https://spreadsheets.google.com/feeds"
        ]
        try:
            self.credentials = service_account.Credentials.from_service_account_file(
                service_account_json_path
                ,scopes=scopes
            )
        except Exception as e: 
            self.credentials, _ = google.auth.default()

        # other variables
        self.location = 'US'
        self.project_id = 'western-verve-411004'
        self.project_name = 'dreams-labs-data'
        self.bucket_name = 'dreams-labs-storage'

        # configure logger
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.NullHandler())


    def run_sql(
            self,
            query_sql
        ):
        '''
        runs a query and returns results as a dataframe. the service account credentials to 
        grant access are autofilled to a general service account. there are likely security
        optimizations that will need to be done in the future. 

        param: query_sql <string> the query to run
        param: location <string> the location of the bigquery project
        param: project <string> the project ID of the bigquery project
        return: query_df <dataframe> the query result
        '''
        # prepare credentials using a service account stored in GCP secrets manager


        # create a bigquery client object and run the query
        client = bigquery.Client(
            project=self.project_id,
            location=self.location,
            credentials=self.credentials
        )
        query_job = client.query(query_sql)
        query_df = query_job.to_dataframe()

        self.logger.debug('BigQuery query completed.')

        return query_df


    def cache_sql(
            self,
            query_sql,
            cache_file_name,
            freshness=24,
        ):
        '''
        tries to use a cached result of a query from gcs. if it doesn't exist or
        is stale, reruns the query and returns fresh results.

        cache location: dreams-labs-storage/cache

        param: query_sql <string> the query to run
        param: cache_file_name <string> what to name the cache
        param: freshness <float> how many hours before a refresh is required
        return query_df <dataframe> the cached or fresh result of the query
        '''

        filepath = f'cache/query_{cache_file_name}.csv'
        client = storage.Client(project=self.project_name, credentials=self.credentials)
        bucket = client.get_bucket(self.bucket_name)

        # Attempt to retrieve file freshness
        try:
            blob = bucket.get_blob(filepath)
            file_freshness = blob.updated if blob else None
        except Exception as e:
            print(f"error retrieving blob: {e}")
            file_freshness = None

        # Determine cache staleness
        cache_stale = (
            file_freshness is None or
            (
                (datetime.datetime.now(tz=datetime.timezone.utc) - file_freshness)
                .total_seconds() / 3600 > freshness
            )
        )
        # Refresh cache if stale
        if cache_stale:
            query_df = self.run_sql(query_sql)
            blob = bucket.blob(filepath)
            blob.upload_from_string(query_df.to_csv(index=False), content_type='text/csv')

            self.logger.debug('returned fresh csv and refreshed cache')

        else:
            query_df = pd.read_csv(f'gs://{self.bucket_name}/{filepath}')

            self.logger.debug('returned cached csv')

        return query_df


    def gcs_upload_file(
            self,
            data,
            gcs_folder,
            filename,
            bucket_name='dreams-labs-storage',
        ):
        '''
        uploads a file to google cloud storage. currently accepted input formats are \
        dataframes or dicts. 

        Params:
            data: <dict> or <dataframe> the data to upload
            gcs_folder: <string> the upload folder in gcs, e.g. 'data_lake/coingecko_market_data'
            filename: <string> the name the gcs file will be given, e.g. 'aioz-network.json'
            project_name: <string> google cloud project name
            bucket_name: <string> GCS bucket name
        '''

        # adjust filename to append filetype if one isn't included
        if '.' in filename:
            pass
        elif isinstance(data, pd.DataFrame):
            filename = f'{filename}.csv'
        elif isinstance(data, dict):
            filename = f'{filename}.json'
        else:
            raise ValueError('Input data must be a dict or dataframe.')

        full_path = f'{gcs_folder}/{filename}'


        try:
            # get the client and bucket
            client = storage.Client(project=self.project_name)
            bucket = client.get_bucket(bucket_name)
            blob = bucket.blob(full_path)

            # if the file is a dataframe, store it as a csv
            if isinstance(data, pd.DataFrame):
                # make temp folder and store the csv there
                temp_folder = 'temp'
                os.makedirs(temp_folder, exist_ok=True)
                local_file_path = f'{temp_folder}/{filename}'
                data.to_csv(local_file_path, index=False)

                # upload the csv to gcs
                with open(local_file_path, 'rb') as file:
                    blob.upload_from_file(file)

                # remove the temporary CSV file and folder
                os.remove(local_file_path)
                os.rmdir(temp_folder)

                self.logger.info('Successfully uploaded %s', f'{bucket_name}/{full_path}')

            # if the file is a dict, store it as a json blob
            elif isinstance(data, dict):
                blob.upload_from_string(json.dumps(data),content_type='json')

                self.logger.info('Successfully uploaded %s', f'{bucket_name}/{full_path}')

        except Exception as e:
            self.logger.error('Failed to upload %s to %s/%s: %s', filename, bucket_name, gcs_folder, e)
            raise


    def get_table_schema(
            self,
            dataset_id,
            table_id
        ):
        """
        Retrieves the schema of a specified BigQuery table.

        Args:
            project_id (str): The GCP project ID where the BigQuery table is located.
            dataset_id (str): The dataset ID in BigQuery where the table is located.
            table_id (str): The table ID in BigQuery for which the schema is to be retrieved.

        Returns:
            schema (list of dicts): A list of dictionaries where each dictionary represents a column \
                in the table schema. Each dictionary contains the column 'name' and its 'type'.
        """
        client = bigquery.Client(project=self.project_id)
        table_ref = client.dataset(dataset_id).table(table_id)
        table = client.get_table(table_ref)

        schema = [{'name': field.name, 'type': field.field_type.lower()} for field in table.schema]

        return schema


    def upload_df_to_bigquery(
            self,
            upload_df,
            dataset_id,
            table_id,
            if_exists='append'
        ):
        '''
        Appends the provided DataFrame to the specified BigQuery table. 

        Steps:
            1. Check if the table exists in BigQuery
            2. If the table exists, retrieve the schema and map datatypes onto new dataframe upload_df
            3. If the table does not exist, use the schema of the upload_df for the new table
            4. Upload the DataFrame using pandas_gbq

        Params:
            upload_df (pandas.DataFrame): The DataFrame to upload
            dataset_id (str): BigQuery dataset ID, e.g. 'etl_pipelines'
            table_id (str): BigQuery table ID, e.g. 'community_calls'
            if_exists (str): If the table already exists, either 'append', 'replace', or 'fail'

        Returns:
            None
        '''
        logger = logging.getLogger(__name__)

        try:
            # 1. Try to retrieve schema from BigQuery
            schema = self.get_table_schema(dataset_id, table_id)

            # Add updated_at column first to ensure it exists before dtype mapping
            upload_df['updated_at'] = datetime.datetime.now(utc)

            # 2. Set df datatypes based on schema
            dtype_mapping = {field['name']: field['type'] for field in schema}
            dtype_mapping = {
                key: (
                    str if value == 'string' else
                    int if value == 'integer' else
                    float if value == 'float64' else
                    'datetime64[us, UTC]' if value == 'datetime' else value
                )
                for key, value in dtype_mapping.items()
            }

            # Clean data for type conversion
            for col in upload_df.columns:
                if dtype_mapping.get(col) == float:
                    upload_df[col] = upload_df[col].replace({r'[^\d.]': ''}, regex=True).astype(float)
                elif dtype_mapping.get(col) == int:
                    upload_df[col] = upload_df[col].replace({r'[^\d]': ''}, regex=True).astype(int)

            # Apply the dtype mapping
            upload_df = upload_df.astype(dtype_mapping)
            logger.info('Prepared upload df with %s rows.', len(upload_df))

        except NotFound:
            logger.warning(f'Table {table_id} does not exist. Creating a new table with the DataFrame schema.')
            schema = None  # Set schema to None to trigger table creation
        except Exception as e:
            logger.error(f'Failed to retrieve schema or apply dtype mapping: {e}')
            raise

        # 3. Upload df to BigQuery
        table_name = f'{dataset_id}.{table_id}'
        pandas_gbq.to_gbq(
            upload_df,
            table_name,
            project_id=self.project_id,
            if_exists=if_exists,
            table_schema=[{
                'name': col,
                'type': (
                    'STRING' if pd.api.types.is_string_dtype(upload_df[col]) else
                    'FLOAT' if pd.api.types.is_float_dtype(upload_df[col]) else
                    'INTEGER' if pd.api.types.is_integer_dtype(upload_df[col]) else
                    'DATETIME' if pd.api.types.is_datetime64_any_dtype(upload_df[col]) else
                    'BOOLEAN' if pd.api.types.is_bool_dtype(upload_df[col]) else
                    'STRING'  # fallback for any other types
                )
            } for col in upload_df.columns] if schema is None or 'replace' in if_exists or 'fail' in if_exists else None,
            progress_bar=False
        )
        logger.info('Uploaded df to %s.', table_name)


    def trigger_cloud_function(self, url, params=None, timeout=300):
        """
        Synchronously trigger a function via an authenticated request.

        Args:
            url (str): The url of the cloud function to which the request is sent.
            params (dict): A dictionary of query parameters to include in the request.
            timeout (int): How many seconds to wait for the function to complete before \
                returning a timeout error.

        Description:
            1. Obtain credentials using service account file specified in the 
            'GOOGLE_APPLICATION_CREDENTIALS' environment variable.
            2. Create an authenticated session using the obtained credentials.
            3. Make an authenticated GET request to the provided URL with query parameters.
            4. Log the response status and content.
        """
        # Obtain credentials
        creds = service_account.IDTokenCredentials.from_service_account_file(
            os.getenv('GOOGLE_APPLICATION_CREDENTIALS'), target_audience=url)

        # Create an authenticated session
        authed_session = AuthorizedSession(creds)

        # Append query parameters to the URL, if provided
        if params:
            url += '?' + urlencode(params)

        # Make an authenticated request
        resp = authed_session.get(url, timeout=timeout)

        # Log the response
        self.logger.info('%s: %s' % (resp.status_code, resp.text))

        return resp.text


    async def trigger_cloud_function_async(self, url, params=None, timeout=300):
        """
        Asynchronously trigger a function via an authenticated request.

        Args:
            url (str): The url of the cloud function to which the request is sent.
            params (dict): A dictionary of query parameters to include in the request.
            timeout (int): How many seconds to wait for the function to complete before \
                returning a timeout error.

        Description:
            1. Obtain credentials using service account file specified in the 
            'GOOGLE_APPLICATION_CREDENTIALS' environment variable.
            2. Create an authenticated session using the obtained credentials.
            3. Make an authenticated GET request to the provided URL with query parameters.
            4. Log the response status and content.
        """
        # Obtain credentials
        creds = service_account.IDTokenCredentials.from_service_account_file(
            os.getenv('GOOGLE_APPLICATION_CREDENTIALS'), target_audience=url)

        # Refresh credentials to fix occasional 401 errors
        creds.refresh(Request())

        # Append query parameters to the URL, if provided
        if params:
            url += '?' + urlencode(params)

        # Create an authenticated session
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"Authorization": f"Bearer {creds.token}"}, timeout=timeout) as resp:
                # Log the response
                self.logger.info('%s: %s' % (resp.status, await resp.text()))

                return resp.text


    def read_google_sheet(self, spreadsheet_id, range_name):
        """
        Reads data from a specified Google Sheet and returns it as a Pandas DataFrame.

        Args:
            spreadsheet_id (str): The ID of the Google Sheet. 
                Example: '1X6AJWBJHisADvyqoXwEvTPi1JSNReVU_woNW32Hz_yQ'
            
            range_name (str): The range of cells to read, formatted as 'SheetName!Range'.
                Example: 'gcs_export!A:K'

        Returns:
            pd.DataFrame: The data from the specified range as a Pandas DataFrame. The first row of the range is used as the header.

        """
        # Create credentials using the service account
        client = gspread.authorize(self.credentials)

        # Open the spreadsheet and get the data
        sheet = client.open_by_key(spreadsheet_id)
        worksheet = sheet.worksheet(range_name.split('!')[0])
        data = worksheet.get(range_name.split('!')[1])

        # Convert to DataFrame
        df = pd.DataFrame(data[1:], columns=data[0])

        self.logger.info(f'Loaded df with dimensions {df.shape} from Google Sheet {spreadsheet_id} {range_name}.')

        return df
