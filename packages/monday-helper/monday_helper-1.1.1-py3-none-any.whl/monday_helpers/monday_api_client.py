import requests
from monday_helpers.graphql_queries import GraphQLQueries
from typing import Dict, Any



class MondayAPIClient:

    """
    A class to interact with the Monday.com API
    """

    def __init__(self, api_key: str, api_url: str = "https://api.monday.com/v2"):
        """
        Initilizes the api client in monday api
        """
        self.api_key = api_key
        self.api_url = api_url

    def get_headers(self) -> Dict[str, str]:
        """
        Return headers required in monday api
        """        
        return {"Authorization": self.api_key, "API-Version": "2023-10"}
    
    def make_request(self, query: str, variables: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Makes request to the Monday Api with Graphql query
        """

        if variables is None:
            variables = {}

        headers = self.get_headers()

        data = {
            'query': query,
            'variables': variables
        }

        response = requests.post(self.api_url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: status-code-{response.status_code} - {response.text}")

    def get_group(self, board_id: str) -> Dict[str, Any]:
        query = GraphQLQueries.get_board_details(board_id)
        response = self.make_request(query)
        return response