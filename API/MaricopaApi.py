#import requests 
#response = requests.get('https://api.mcassessor.maricopa.gov/api/search/mh/phoenix/', headers={'Authorization': 'TOK:5ae1363b-28b8-11e8-9917-00155da2c015'})
#print(response.content)

import urllib.request
import json


def get_response_json_object(url, auth_token):

	req=urllib.request.Request(url, None, {"X-MC-AUTH": "%s" %auth_token})
	response=urllib.request.urlopen(req)
	html=response.read()
	json_obj=json.loads(html)
	return json_obj

#json_obj = get_response_json_object('https://api.mcassessor.maricopa.gov/api/search/mh/phoenix/offset=190','5ae1363b-28b8-11e8-9917-00155da2c015')

#https://api.mcassessor.maricopa.gov/api/parcel/{apn}
json_obj = get_response_json_object('https://api.mcassessor.maricopa.gov/api/parcel/158-27-100-C','5ae1363b-28b8-11e8-9917-00155da2c015')

print(json_obj)