import requests

import configuration

print(configuration.URL_SERVICE)
print(configuration.DOC_PATH)
import requests

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
responce = get_docs()
print(responce.status_code)