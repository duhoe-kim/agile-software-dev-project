from flask import request
import json

def get_and_parse_json_data():
    # Retrieve the JSON data from the URL query parameter
    json_data = request.args.get('jsonData')

    # Parse the JSON data (if provided)
    parsed_data = []

    if json_data:
       parsed_data = json.loads(json_data)
    return parsed_data


