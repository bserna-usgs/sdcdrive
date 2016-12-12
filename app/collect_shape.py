# ============================================================================
# U.S. Geological Survey - Science Data Catalog
# ============================================================================
#
# BETA 1.1 - portion of files non fuse mount
#
# Developed in 3.4 will run currently on osx installed 2.7
# Need to run with 2.7 system lvl python, keep this requests - urllib and requests
# 3.4 urllib.request.urlretrieve
# 2.7 urllib.urlretrieve
import sys, os, zipfile, urllib, csv, datetime, shutil
import requests


def main():
    example = []

    # Get Solr
    url = """http://mercury.ornl.gov/usgssolr4/core1dev/select?q=*%3A*&rows=7500&fl=data_url%2Cid%2Ccollection_id%2CcsvURL&wt=json&indent=true"""
    print('Fetching Science Data Catalog index')

    def fetch_solr_index(get_url):
        r = requests.get(get_url)
        json_output = r.json()
        sclvl = json_output['response']['docs']
        return sclvl

    second_lvl = fetch_solr_index(url)

    # Parse Solr
    count = 0
    for i in second_lvl:
        try:
            grouping = second_lvl[count]
            idd = grouping['id']
            collection = grouping['collection_id']
            data_url = grouping['data_url']

            if len(data_url) > 1:
                for link in data_url:
                    if link.endswith('.txt'):
                        url_title = link.rpartition('/')[-1]
                    try:
                        response_check = requests.head(link)
                        if response_check.status_code == 200:
                            good_to_download = True
                        else:
                            good_to_download = False
                    except Exception as e:
                        print('Header exception: ', str(e))
                        good_to_download = False

                    if good_to_download:
                        try:
                            response_header = response_check.headers
                            file_size = int(response_header['content-length'])
                            if file_size < 10000:
                                try:
                                    # Collection folder exists
                                    if os.path.isdir(collection):
                                        # Record id folder exists
                                        if os.path.isdir(os.path.join(collection, idd)):
                                            w_record = os.path.join(collection, idd)
                                            full_file = os.path.join(w_record, url_title)

                                            # Download
                                            # urllib.request.urlretrieve(url, full_file)
                                            # Conversion for 2.7
                                            urllib.urlretrieve(link, full_file)

                                            # Also download the metadata
                                            meta_url = os.path.join("http://usgs.ornl.gov/metadata/devcatalog/xml/", w_record)
                                            first = os.path.join(collection,idd)
                                            # urllib.request.urlretrieve(meta_url, os.path.join(first, idd))
                                            urllib.urlretrieve(meta_url, os.path.join(first, idd))

                                        else:
                                            full_filename = os.path.join(collection, idd)

                                            # Make record_id folder
                                            os.makedirs(full_filename)

                                            # Join path for placement for the download
                                            with_id = os.path.join(full_filename, url_title)

                                            # Download
                                            # urllib.request.urlretrieve(url, with_id)
                                            urllib.urlretrieve(link, with_id)

                                            # Also download the metadata
                                            w_record = os.path.join(collection, idd)
                                            meta_url = os.path.join("http://usgs.ornl.gov/metadata/devcatalog/xml/", w_record)
                                            first = os.path.join(collection,idd)
                                            #urllib.request.urlretrieve(meta_url, os.path.join(first, idd))
                                            urllib.urlretrieve(meta_url, os.path.join(first, idd))
                                    else:
                                        # When collection folder does not exist

                                        # Make collection folder
                                        os.makedirs(collection)

                                        # Make record folder
                                        full_filename = os.path.join(collection, idd)
                                        os.makedirs(full_filename)

                                        with_id = os.path.join(full_filename, url_title)
                                        # urllib.request.urlretrieve(url, with_id)
                                        urllib.urlretrieve(link, with_id)

                                        # Also download the metadata
                                        w_record = os.path.join(collection, idd)
                                        meta_url = os.path.join("http://usgs.ornl.gov/metadata/devcatalog/xml/", w_record)
                                        first = os.path.join(collection,idd)
                                        # urllib.request.urlretrieve(meta_url, os.path.join(first, idd))
                                        urllib.urlretrieve(meta_url, os.path.join(first, idd))

                                    add_tolist = (idd, url_title, collection)
                                    example.append(add_tolist)
                                except Exception as e:
                                    pass
                        except Exception as e:
                            pass
        except Exception as e:
            pass
        count += 1

if __name__ == '__main__':
    main()
