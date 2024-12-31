import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from fb_data.utils import camel_to_snake


class GoogleAnalytics:
    def __init__(self, **kwargs):
        """
        Initialize the Google Analytics connector.

        Args:
            **kwargs: Keyword arguments containing user credentials.
                      Example: client_id, client_secret, refresh_token, etc.
        """
        # Set the token URI internally
        token_uri = "https://oauth2.googleapis.com/token"

        # Combine user-provided credentials with the internal token URI
        self.credentials = {**kwargs, "token_uri": token_uri}
        self.user_credentials = Credentials.from_authorized_user_info(info=self.credentials)
        self.service = build('analyticsdata', 'v1beta', credentials=self.user_credentials)

    def query(self, property_id: str, request_body: dict, output: str = "raw"):
        """
        Execute a query against the Google Analytics API.

        Args:
            property_id (str): The property ID for the Analytics account.
            request_body (dict): Pre-constructed request body with dimensions, metrics, and date ranges.
            output (str): Output format ('raw' or 'pandas'). Default is 'raw'.

        Returns:
            dict or pd.DataFrame: Raw API response or formatted Pandas DataFrame.
        """
        if output not in ["raw", "pandas"]:
            raise ValueError("Invalid output format. Use 'raw' or 'pandas'.")

        # Execute the query
        response = self.service.properties().batchRunReports(
            property=f'properties/{property_id}', body=request_body
        ).execute()

        # Return raw response if output is 'raw'
        if output == "raw":
            return response

        # Extract headers for dimensions and metrics
        dimension_headers = [header["name"] for header in response["reports"][0]["dimensionHeaders"]]
        metric_headers = [header["name"] for header in response["reports"][0]["metricHeaders"]]

        # Initialize a list to hold row data
        rows_data = []

        # Parse rows from the response
        for row in response["reports"][0]["rows"]:
            # Extract dimension values
            dimension_values = [value["value"] for value in row["dimensionValues"]]
            # Extract metric values
            metric_values = [value["value"] for value in row["metricValues"]]
            # Combine dimensions and metrics into a single row
            rows_data.append(dimension_values + metric_values)

        # Combine headers for the DataFrame
        all_headers = dimension_headers + metric_headers

        # Create a DataFrame
        df = pd.DataFrame(rows_data, columns=all_headers)

        # Rename columns to snake_case
        df.rename(columns={col: camel_to_snake(col) for col in df.columns}, inplace=True)

        # Format the date column if present
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], format="%Y%m%d", errors="coerce")

        return df


