import os
import requests
import urllib
import zipfile


def process_files(url, collection_id, idd, file_size_get):
    # Figure out actual filesize
    if file_size_get == "5mb":
        file_size_get = 5000000
    elif file_size_get == "10mb":
        file_size_get = 10000000
    elif file_size_get == "50mb":
        file_size_get = 50000000
    elif file_size_get == "1gb":
        file_size_get = 1000000000
    else:
        file_size_get = 5000000

    if url.endswith('.html') or url.endswith('.zip') or url.endswith('.csv') or url.endswith('.shp') or url.endswith(
            '.dbf') or url.endswith('.shx') or url.endswith('.jpg') or url.endswith('.png') or url.endswith(
            '.jpeg') or url.endswith('.xml') or url.endswith('.sgml') or url.endswith('.txt'):
        # Create clean title name
        url_title = url.rpartition('/')[-1]

        # Check and return header codes
        try:
            response_check = requests.head(url, verify=False, timeout=10)
            # 200 codes
            if response_check.status_code == 200 or response_check.status_code == 201 or response_check.status_code == 202:
                print('Response good, status code: ' + str(response_check))
                status_pass = True

            # 300 redirect codes
            elif response_check.status_code == 300 or response_check.status_code == 302 or response_check.status_code == 301:
                print('Redirect, status code: ' + str(response_check))
                status_pass = True

                # need to dive further for the redirection url
                print(url)
                url = response_check.headers['location']
                print(url)
                response_check = requests.head(url, verify=False, timeout=100)
                print('do we make it here?')
            else:
                status_pass = False
        except Exception as e:
            print('Response exception raised, no response code to view: ' + str(e))
            status_pass = False
        # When the tests pass we can then move forward
        if status_pass is True:
            try:
                # Issue with the redirects not returning full http field on header request
                response_header = response_check.headers
                file_size = int(response_header['content-length'])
                # 1gb = 1000000000
                if file_size < file_size_get:
                    if url.endswith('.zip'):
                        print('Zip file url: ' + str(url))
                        urllib.urlretrieve(url, url_title)
                        with zipfile.ZipFile(url_title) as zf:
                            zf.extractall(os.path.join('sdc', os.path.join(collection_id, idd)))
                            zf.close()
                            # Metdata get
                            #urllib.urlretrieve(str("http://usgs.ornl.gov/metadata/devcatalog/xml/" + "/" + collection_id + "/" + idd), str("sdc" + "/" + collection_id + "/" + idd))
                    else:
                        # Verify the directory is created
                        start_files = os.path.join('sdc', os.path.join(collection_id, idd))
                        if os.path.exists(start_files):
                            print("directory already created...")
                        else:
                            os.system("mkdir " + start_files)
                        # Download
                        urllib.urlretrieve(url, os.path.join(start_files, url_title))
                        # Metdata get
                        #w_record = os.path.join(collection_id, idd)
                        #meta_url = os.path.join("http://usgs.ornl.gov/metadata/devcatalog/xml/", w_record)
                        #start_files = os.path.join('sdc', os.path.join(collection_id, idd))
                        #urllib.urlretrieve(str("http://usgs.ornl.gov/metadata/devcatalog/xml/" + "/" + collection_id + "/" + idd), str("sdc" + "/" + collection_id + "/" + idd))
            except Exception as e:
                print('File size couldn\'t resolve from header request: ' + str(e))
