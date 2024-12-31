import os
from datetime import datetime, date, timedelta
import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


class GoogleSearchConsole:
    def __init__(self, client_id, client_secret, refresh_token, site_url):
        """
        Initialize the Google Search Console API client.

        Args:
            client_id (str): Google API client ID.
            client_secret (str): Google API client secret.
            refresh_token (str): OAuth refresh token.
            site_url (str): The site URL to query data for. Default is "https://fishingbooker.com/".
        """
        self.site_url = site_url
        credentials_obj = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
        }

        credentials = Credentials.from_authorized_user_info(
            credentials_obj, ["https://www.googleapis.com/auth/webmasters.readonly"]
        )

        # Refresh credentials
        request_object = Request()
        credentials.refresh(request_object)

        # Build service
        self.service = build("searchconsole", "v1", credentials=credentials)

    def find_latest_date(self, agg_type="auto", data_state="final") -> str:
        """
        Find the latest date available in the Search Console API.

        Args:
            agg_type (str): Aggregation type for the query. Default is 'auto'.
            data_state (str): Data state (e.g., 'final' or 'all'). Default is 'final'.

        Returns:
            str: The latest date available in the dataset.
        """
        request = {
            "startDate": (date.today() - timedelta(days=10)).strftime("%Y-%m-%d"),
            "endDate": date.today().strftime("%Y-%m-%d"),
            "dimensions": ["date"],
            "aggregationType": agg_type,
            "dataState": data_state,
        }

        results = self.service.searchanalytics().query(siteUrl=self.site_url, body=request).execute()
        return results["rows"][-1]["keys"][0] if "rows" in results else None

    def query(
            self,
            start_date: str,
            end_date: str,
            dimensions: list,
            row_limit: int = 25000,
            filters: list = None,
            agg_type: str = "auto",
            search_type: str = "web",
            offset: int = 0,
            data_state: str = "final",
            output: str = "raw",
    ):
        """
        Query the Search Console API for data.

        Args:
            start_date (str): Start date of the query (format: YYYY-MM-DD).
            end_date (str): End date of the query (format: YYYY-MM-DD).
            dimensions (list): Dimensions to query.
            row_limit (int): Maximum rows to fetch in each API call. Default is 25000.
            filters (list): List of filters to apply. Default is None.
            agg_type (str): Aggregation type (e.g., 'auto' or 'byPage'). Default is 'auto'.
            search_type (str): Search type (e.g., 'web', 'video'). Default is 'web'.
            offset (int): Starting row for pagination. Default is 0.
            data_state (str): Data state (e.g., 'final' or 'all'). Default is 'final'.
            output (str): Output format ('raw' or 'pandas'). Default is 'raw'.

        Returns:
            list or pd.DataFrame: Query results as raw data or Pandas DataFrame.
        """
        if output not in ["raw", "pandas"]:
            raise ValueError("Invalid output format. Use 'raw' or 'pandas'.")

        data = []
        while True:
            request = {
                "startDate": start_date,
                "endDate": end_date,
                "dimensions": dimensions,
                "rowLimit": row_limit,
                "aggregationType": agg_type,
                "dimensionFilterGroups": filters if filters else [],
                "type": search_type,
                "startRow": offset,
                "dataState": data_state,
            }

            results = self.service.searchanalytics().query(siteUrl=self.site_url, body=request).execute()

            if "rows" in results:
                data.extend(results["rows"])
                offset += len(results["rows"])
                if len(results["rows"]) < row_limit:
                    break
            else:
                break

        print(f"Extraction completed - {len(data)} rows total")

        if output == "raw":
            return data

        # Convert raw data to Pandas DataFrame
        rows = []
        for row in data:
            # Flatten the `keys` into individual columns (dimensions)
            row_data = {dim: value for dim, value in zip(dimensions, row["keys"])}
            # Add the metrics to the row
            row_data.update({metric: row[metric] for metric in row if metric != "keys"})
            rows.append(row_data)

        df = pd.DataFrame(rows)

        return df

