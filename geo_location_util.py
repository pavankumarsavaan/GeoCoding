import json
import sys
import requests
from colorama import Fore, init


class GeoLocationUtil:
    """
    This is a class for Geo Coding with location and zipcode

    Attributes:
        base_uri (string): base uri of Geo Location API
        geo_loc_input (string): location or zipcode
    """

    def __init__(self, base_uri, geo_loc_input, limit=5, app_id='f897a99d971b5eef57be6fafa0d83239'):
        """
            Constructor for Geo Coding with location and zipcode
            Attributes:
                base_uri (string): base uri of Geo Location API
                geo_loc_input (string): location or zipcode
                limit (integer): 5 default if not passed
                app_id (string): 'f897a99d971b5eef57be6fafa0d83239' default if not passed
        """
        self.base_uri = base_uri
        self.default_query_params = {
            'limit': limit,
            'appid': app_id
        }
        self.geo_loc_input = geo_loc_input

    def print_response(self, response):
        """
            The function to pretty print the geocoding api's output
            :param response: response object
        """
        pretty_json = json.dumps(response.json(), indent=4)
        if response.status_code == 200:
            print(Fore.GREEN + f"Response for input: {self.geo_loc_input} -> Success")
            print(pretty_json)
        else:
            print(Fore.RED + f"Response for input: {self.geo_loc_input} -> Failed")
            print(pretty_json)

    def get_coordinates_by_location(self, location):
        """
            The function to get coordinates with location
            :param location: city, state
        """
        url = self.base_uri + "/direct"
        params = self.default_query_params
        params.update({'q': f"{location},US"})
        response = make_request(url, params)
        self.print_response(response)

    def get_coordinates_by_zipcode(self, zipcode):
        """
            The function to get coordinates with zipcode
            :param zipcode: zip
        """
        url = self.base_uri + "/zip"
        params = self.default_query_params
        params.update({'zip': zipcode})
        response = make_request(url, params)
        self.print_response(response)


def make_request(url, query_params):
    """
    Make a get request for geolocation
    :param url: Full url of the request
    :param query_params: query parameters
    :return: response object
    """
    return requests.get(url, params=query_params)

def input_data():
    """
    Reads the base_uri, limit & app id values from data.json file
    :return: dict
    """
    file_path = 'data.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    init(autoreset=True)
    data_params = input_data()
    # Error out if the count of input args is less than 2
    if len(sys.argv) < 2:
        raise ValueError(Fore.RED + "Please provide at least 2 arguments")
    else:
        # Iterate through the arguments
        for arg in sys.argv[1:]:
            # Create object for GeoLocationUtil
            geo_location = GeoLocationUtil(data_params["base_uri"], arg, data_params["limit"], data_params["app_id"])
            # Call geo coordinates by location if the input arg contains a comma
            if ',' in arg:
                geo_location.get_coordinates_by_location(arg)
            # Call geo coordinates by zipcode
            else:
                geo_location.get_coordinates_by_zipcode(arg)