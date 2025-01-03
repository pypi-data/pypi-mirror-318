import pandas as pd

from google.cloud import bigquery
from google.oauth2 import service_account

from typing import Tuple, Union


class BQTools(object):
    """
    Interact with BigQuery, such as saving and pulling data.
    """
    def __init__(self) -> None:
        pass

    def _setup_connection(self, bq_creds: dict) -> Union[bigquery.Client, str]:
        """Set up a connection to the bigquery database."""
        scope = ['https://www.googleapis.com/auth/bigquery']
        try:
            creds = service_account.Credentials.from_service_account_info(
                bq_creds, scopes=scope)
        except Exception as e:
            return f"Error loading credentials: {str(e)}"
        try:
            client = bigquery.Client(credentials=creds)
        except Exception as e:
            return f"Error creating the BigQuery client: {str(e)}"
        return client

    def _setup_job_config(self, if_exists: str) -> bigquery.LoadJobConfig:
        # determine behavior if table already exists
        if if_exists == 'append':
            write_disposition = 'WRITE_APPEND'
        elif if_exists == 'replace':
            write_disposition = 'WRITE_TRUNCATE'
        else:
            write_disposition = 'WRITE_EMPTY'
        # set up the config
        job_config = bigquery.LoadJobConfig(
            write_disposition=write_disposition
        )
        return job_config

    def _store_df(self,
                  client: bigquery.Client,
                  df: pd.DataFrame,
                  table_id: str,
                  job_config: bigquery.LoadJobConfig) -> Union[None, str]:
        try:
            job = client.load_table_from_dataframe(df, table_id,
                                                   job_config=job_config)
            job.result()
        except Exception as e:
            return f"Error storing BigQuery data: {str(e)}"

    def _test_data_stored(self, client: bigquery.Client,
                          table_id: str) -> Union[None, str]:
        """Test if we can access the table / double check that it
            saved."""
        try:
            _ = client.get_table(table_id)  # Make an API request.
        except Exception as e:
            return f"Error getting the saved table from BigQuery: {str(e)}"

    def _run_query(self, client: bigquery.Client,
                   sql_statement: str) -> Union[bigquery.QueryJob, tuple]:
        try:
            query_job = client.query(sql_statement)
            query_job.result()
            return query_job
        except Exception as e:
            return ('dev_error', f"Error retrieving BigQuery data: {str(e)}")

    def store_lock_times(
            self,
            email: str,
            email_col: str,
            locked_time_col: str,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            if_exists: str = 'append') -> Union[None, str]:
        """
        Stores a lock time to Google BigQuery.

        :param email: The email to store the lock time for.
        :param email_col: The column that holds the email.
        :param locked_time_col: The column that holds the locked_times.
        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to store the data in.
        :param dataset: The dataset to store the data in.
        :param table_name: The name of the table to store the data in.
        :param if_exists: What to do if the table already exists.
            Can be 'append', 'replace', or 'fail'. Default is 'append'.
        :return: None if successful, error message if not.
        """
        # turn the username and time into a dataframe
        store_info = {email_col: [email],
                      locked_time_col: [pd.to_datetime('now', utc=True)]}
        df = pd.DataFrame(store_info)

        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return client

        # set up table_id
        table_id = project + "." + dataset + "." + table_name

        job_config = self._setup_job_config(if_exists)

        # store
        job_result = self._store_df(client, df, table_id, job_config)
        if isinstance(job_result, str):
            return job_result

        # test if we can access the table / double check that it saved
        stored_result = self._test_data_stored(client, table_id)
        if isinstance(stored_result, str):
            return stored_result

    def pull_register_user_locked_info_bigquery(
            self,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            email_col: str,
            email: str,
            locked_time_col: str) -> Tuple[str, Union[str, tuple]]:
        """
        Pull the latest locked_time for an email from BigQuery.

        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to pull the data from.
        :param dataset: The dataset to pull the data from.
        :param table_name: The table to pull the data from.
        :param email_col: The column that holds the email.
        :param email: The email to pull the info for.
        :param locked_time_col: The column that holds the locked_times.
        :return: A tuple with an indicator labeling the result as either
            'success' or 'error', and the latest lock time if successful
            or the error message if not.
        """
        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return ('dev_error', client)

        table_id = project + "." + dataset + "." + table_name

        # create and run the query
        sql_statement = (
            f"SELECT {locked_time_col} FROM {table_id} "
            f"WHERE {email_col} = '{email}' "
            f"ORDER BY {locked_time_col} DESC")
        # run the query
        query_result = self._run_query(client, sql_statement)
        if isinstance(query_result, tuple):
            return query_result

        # create the df pull the first values
        df = query_result.to_dataframe()
        try:
            # sort the locked_time_col column of df
            df.sort_values(by=locked_time_col, ascending=False, inplace=True)
            # the latest_lock should be the most recent locked_time
            latest_lock = df.iloc[0, 0]
        except Exception as e:
            latest_lock = None

        return ('success', latest_lock)

    def store_user_credentials(
            self,
            user_credentials: dict,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            if_exists: str = 'append') -> Union[None, str]:
        """
        Stores user credentials to Google BigQuery.

        :param user_credentials: The user credentials to store, which
            should come in with anything you need to save to bigquery,
            except for a datetime stamp, which we add here. Each key
            should just have one value associated with it, so we are only
            storing one row of data. For example, you could have:
            {'username': 'my_username', 'email': 'my_email',
            'password': 'my_password'}.
        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to store the data in.
        :param dataset: The dataset to store the data in.
        :param table_name: The name of the table to store the data in.
        :param if_exists: What to do if the table already exists.
            Can be 'append', 'replace', or 'fail'. Default is 'append'.
        :return: None if successful, error message if not.
        """
        # turn the user credentials into a dataframe
        for key in user_credentials:
            # create an error if the value is a list or dict
            if isinstance(user_credentials[key], (list, dict)):
                return ("Each key in user_credentials should have only one "
                        "value.")
            else:
                user_credentials[key] = [user_credentials[key]]
        # we to add a utc timestamp
        user_credentials['datetime'] = [pd.to_datetime('now', utc=True)]
        df = pd.DataFrame(user_credentials)

        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return client

        # set up table_id
        table_id = project + "." + dataset + "." + table_name

        # set up job_config
        job_config = self._setup_job_config(if_exists)

        # store
        job_result = self._store_df(client, df, table_id, job_config)
        if isinstance(job_result, str):
            return job_result

        # test if we can access the table / double check that it saved
        stored_result = self._test_data_stored(client, table_id)
        if isinstance(stored_result, str):
            return stored_result

    def pull_value_based_on_other_col_value(
            self,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            reference_col: str,
            reference_value: str,
            target_col: Union[str, list]) -> Tuple[str, str]:
        """
        Pull a value from a BigQuery column (target), based on the value
            in another column (reference). The target can be one or more
            data fields. This is meant to be a unique match (per field),
            so only returns the first value found (per field).

        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to pull the data from.
        :param dataset: The dataset to pull the data from.
        :param table_name: The table to pull the data from.
        :param reference_col: The column that holds the values to compare
            against.
        :param reference_value: The value to match in the reference_col.
        :param target_col: The column(s) that holds the value to pull.
        :return: A tuple with an indicator labeling the result as either
            'success' or 'error', and the hashed password if successful or
            the error message if not.
        """
        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return ('dev_error', client)

        # create the query
        table_id = project + "." + dataset + "." + table_name
        if isinstance(target_col, list):
            target_col = ', '.join(target_col)
            multiple_results = True
        else:
            multiple_results = False
        sql_statement = (f"SELECT {target_col} FROM {table_id} "
                         f"WHERE {reference_col} = '{reference_value}'")

        # run the query
        query_result = self._run_query(client, sql_statement)
        if isinstance(query_result, tuple):
            return query_result

        # create the df pull the first value(s)
        df = query_result.to_dataframe()
        try:
            if multiple_results:
                target_value = tuple(df.iloc[0, :])
            else:
                target_value = df.iloc[0, 0]
        except Exception as e:
            # we don't have a message here because this is handled by the
            # calling function - it should combine the lack of a value
            # with the potential for an incorrect reference and display
            # something like "Incorrect username or password" (if password
            # is the target and username is the reference).
            return ('user_error', None)

        return ('success', target_value)

    def pull_full_column_bigquery(
            self,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            target_col: str) -> Tuple[str, pd.Series]:
        """
        Pull a full column of data from BigQuery.

        Note that this method isn't currently used in Forms or
        Verification, but is useful for gathering usernames for a login
        page.

        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to pull the data from.
        :param dataset: The dataset to pull the data from.
        :param table_name: The table to pull the data from.
        :param target_col: The column that holds the data.
        :return: A tuple with an indicator labeling the result as either
            'success' or 'error', and the password if successful or the
            error message if not.
        """
        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return ('dev_error', client)

        # create the query
        table_id = project + "." + dataset + "." + table_name
        sql_statement = f"SELECT {target_col} FROM {table_id}"

        # run the query
        query_result = self._run_query(client, sql_statement)
        if isinstance(query_result, tuple):
            return query_result

        # create the df
        df = query_result.to_dataframe()
        try:
            data = df.iloc[:, 0]
        except Exception as e:
            # we don't have a message here because this is handled by the
            # calling function - it should combine the lack of password
            # with the potential for an incorrect username and display
            # something like "Incorrect username or password."
            return ('user_errors', None)

        return ('success', data)

    def pull_login_locked_info_bigquery(
            self,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            username_col: str,
            username: str,
            locked_time_col: str,
            unlocked_time_col: str) -> Tuple[str, Union[str, tuple]]:
        """
        Pull the latest locked_time and unlocked_time for a username from
        BigQuery.

        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to pull the data from.
        :param dataset: The dataset to pull the data from.
        :param table_name: The table to pull the data from.
        :param username_col: The column that holds the username.
        :param username: The username to pull the info for.
        :param locked_time_col: The column that holds the locked_times.
        :param unlocked_time_col: The column that holds the
            unlocked_times.
        :return: A tuple with an indicator labeling the result as either
            'success' or 'error', and a tuple of (latest lock time,
            latest unlock time) if successful or the error message if not.
        """
        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return ('dev_error', client)

        table_id = project + "." + dataset + "." + table_name

        # create and run the query
        sql_statement = (
            f"SELECT {locked_time_col}, {unlocked_time_col} FROM {table_id} "
            f"WHERE {username_col} = '{username}' "
            f"ORDER BY {locked_time_col} DESC, {unlocked_time_col} DESC")
        # run the query
        query_result = self._run_query(client, sql_statement)
        if isinstance(query_result, tuple):
            return query_result

        # create the df pull the first values
        df = query_result.to_dataframe()
        try:
            # sort the locked_time_col column of df
            df.sort_values(by=locked_time_col, ascending=False, inplace=True)
            # the latest_lock should be the most recent locked_time
            latest_lock = df.iloc[0, 0]
        except Exception as e:
            latest_lock = None
        try:
            # sort the unlocked_time_col column of df
            df.sort_values(by=unlocked_time_col, ascending=False, inplace=True)
            # the latest_unlock should be the most recent unlocked_time
            latest_unlock = df.iloc[0, 1]
        except Exception as e:
            latest_unlock = None

        return ('success', (latest_lock, latest_unlock))

    def store_lock_unlock_times(
            self,
            username: str,
            username_col: str,
            locked_time_col: str,
            unlocked_time_col: str,
            lock_or_unlock: str,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            if_exists: str = 'append') -> Union[None, str]:
        """
        Stores a lock or unlock time to Google BigQuery.

        :param username: The username to store the lock or unlock time
            for.
        :param username_col: The column that holds the username.
        :param locked_time_col: The column that holds the locked_times.
        :param unlocked_time_col: The column that holds the
            unlocked_times.
        :param lock_or_unlock: Whether the time is a lock or unlock time.
        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to store the data in.
        :param dataset: The dataset to store the data in.
        :param table_name: The name of the table to store the data in.
        :param if_exists: What to do if the table already exists.
            Can be 'append', 'replace', or 'fail'. Default is 'append'.
        :return: None if successful, error message if not.
        """
        # turn the username and time into a dataframe
        if lock_or_unlock == 'lock':
            store_info = {username_col: [username],
                          locked_time_col: [pd.to_datetime('now', utc=True)],
                          unlocked_time_col: [None]}
        elif lock_or_unlock == 'unlock':
            store_info = {username_col: [username],
                          locked_time_col: [None],
                          unlocked_time_col: [pd.to_datetime('now', utc=True)]}
        else:
            return "lock_or_unlock must be either 'lock' or 'unlock'."
        df = pd.DataFrame(store_info)

        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return client

        # set up table_id
        table_id = project + "." + dataset + "." + table_name

        job_config = self._setup_job_config(if_exists)

        # store
        job_result = self._store_df(client, df, table_id, job_config)
        if isinstance(job_result, str):
            return job_result

        # test if we can access the table / double check that it saved
        stored_result = self._test_data_stored(client, table_id)
        if isinstance(stored_result, str):
            return stored_result

    def store_incorrect_auth_times(
            self,
            username_or_email: str,
            username_or_email_col: str,
            datetime_col: str,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            if_exists: str = 'append') -> Union[None, str]:
        """
        Stores a username or email and datetime associated with a failed
        authorization (either login or registering with an authorization
        code) to Google BigQuery.

        :param username_or_email: The username or email to store.
        :param username_or_email_col: The column that holds the username
            or email.
        :param datetime_col: The column that holds the datetime.
        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to store the data in.
        :param dataset: The dataset to store the data in.
        :param table_name: The name of the table to store the data in.
        :param if_exists: What to do if the table already exists.
            Can be 'append', 'replace', or 'fail'. Default is 'append'.
        :return: None if successful, error message if not.
        """
        # turn the username and datetime into a dataframe
        store_info = {username_or_email_col: [username_or_email],
                      datetime_col: [pd.to_datetime('now', utc=True)]}
        df = pd.DataFrame(store_info)

        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return client

        # set up table_id
        table_id = project + "." + dataset + "." + table_name

        job_config = self._setup_job_config(if_exists)

        # store
        job_result = self._store_df(client, df, table_id, job_config)
        if isinstance(job_result, str):
            return job_result

        # test if we can access the table / double check that it saved
        stored_result = self._test_data_stored(client, table_id)
        if isinstance(stored_result, str):
            return stored_result

    def pull_incorrect_attempts(
            self,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            username_or_email_col: str,
            username_or_email: str,
            datetime_col: str) -> Tuple[str, Union[pd.Series, None, str]]:
        """
        Pull a datetimes associated with an incorrect authorization
        (either login or registering with an authorization code) from
        BigQuery.

        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to pull the data from.
        :param dataset: The dataset to pull the data from.
        :param table_name: The table to pull the data from.
        :param username_or_email_col: The column that holds the usernames
            or emails.
        :param username_or_email: The username or email to match.
        :param datetime_col: The column that holds the datetimes to pull.
        :return: A tuple with an indicator labeling the result as either
            'success' or 'error', and the series with the datetimes of
            incorrect attempts if successful or the error message if not.
        """
        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return ('dev_error', client)

        # create the query
        table_id = project + "." + dataset + "." + table_name
        sql_statement = (
            f"SELECT {datetime_col} FROM {table_id} "
            f"WHERE {username_or_email_col} = '{username_or_email}'")

        # run the query
        query_result = self._run_query(client, sql_statement)
        if isinstance(query_result, tuple):
            return query_result

        # create the df and then get the series with the datetime
        df = query_result.to_dataframe()
        # if data_series is empty, we return None
        if df.empty:
            data_series = None
        else:
            data_series = df[datetime_col]

        return ('success', data_series)

    def update_value_based_on_other_col_value(
            self,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            reference_col: str,
            reference_value: str,
            target_col: str,
            target_value: Union[str, bool],
            datetime_col: str) -> Tuple[str, str]:
        """
        Update a value in a specific column in BigQuery based on a value
            matching in another column. Also stores the datetime to
            record when the change occurred.

        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to pull the data from.
        :param dataset: The dataset to pull the data from.
        :param table_name: The table to pull the data from.
        :param reference_col: The column to check the reference_value
            against.
        :param reference_value: The value to match in the reference_col.
        :param target_col: The column that holds the data to be updated.
        :param target_value: The new value to store in the target_col in
            the same row where reference_value is in reference_col.
        :param datetime_col: The column that holds the datetime, where we
            will update.
        :return: If there's an error, returns a tuple with 'dev_error' as
            the first value and the error message as the second value.
        """
        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return client

        # get the datetime to update that as well
        new_datetime = pd.to_datetime('now', utc=True)

        # create the query
        table_id = project + "." + dataset + "." + table_name
        if isinstance(target_value, str):
            target_value = "'" + target_value + "'"
        sql_statement = (f"UPDATE {table_id} "
                         f"SET {target_col} = {target_value}, "
                         f"{datetime_col} = '{new_datetime}' "
                         f"WHERE {reference_col} = '{reference_value}'")

        # run the query
        query_result = self._run_query(client, sql_statement)
        if isinstance(query_result, tuple):
            return query_result[1]

    def store_preauthorization_codes(
            self,
            emails_codes: dict,
            bq_creds: dict,
            project: str,
            dataset: str,
            table_name: str,
            if_exists: str = 'append') -> Union[None, str]:
        """
        Stores user credentials to Google BigQuery.

        :param emails_codes: The emails and codes to store. The emails
            and codes should be in lists of the same length with each
            position in the list corresponding to the same user.
            {'emails': [emails], 'codes': [codes]}.
        :param bq_creds: The credentials to access the BigQuery project.
            These should, at a minimum, have the roles of "BigQuery Data
            Editor", "BigQuery Read Session User" and "BigQuery Job User".
        :param project: The project to store the data in.
        :param dataset: The dataset to store the data in.
        :param table_name: The name of the table to store the data in.
        :param if_exists: What to do if the table already exists.
            Can be 'append', 'replace', or 'fail'. Default is 'append'.
        :return: None if successful, error message if not.
        """
        df = pd.DataFrame(emails_codes)

        # connect to the database
        client = self._setup_connection(bq_creds)
        if isinstance(client, str):
            # in this case the "client" is an error message
            return client

        # set up table_id
        table_id = project + "." + dataset + "." + table_name

        # set up job_config
        job_config = self._setup_job_config(if_exists)

        # store
        job_result = self._store_df(client, df, table_id, job_config)
        if isinstance(job_result, str):
            return job_result

        # test if we can access the table / double check that it saved
        stored_result = self._test_data_stored(client, table_id)
        if isinstance(stored_result, str):
            return stored_result
