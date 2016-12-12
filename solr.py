'''
Solr
'''
import requests

# url = """http://mercury.ornl.gov/usgssolr4/core1dev/select?q=*%3A*&rows=7500&fl=data_url%2Cid%2Ccollection_id%2CcsvURL&wt=json&indent=true"""
# print('Fetching Science Data Catalog index')


def fetch_solr_index():
    get_url = """http://mercury.ornl.gov/usgssolr4/core1dev/select?q=*%3A*&rows=9500&fl=data_url%2Cid%2Ccollection_id&wt=json&fl=keywords&indent=true"""
    r = requests.get(get_url)
    json_output = r.json()
    sclvl = json_output['response']['docs']
    return sclvl

# second_lvl = fetch_solr_index(url)
