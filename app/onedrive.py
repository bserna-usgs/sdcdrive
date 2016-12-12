'''
Science Data Catalog Drive

Description: A "virtual" drive to enable science data exploration from
    the USGS Science Data Catalog. This project was inspired by
    previous collaborative work with DataONE on the ONEDrive project.
    Technically this application bundle requires python and the Requests
    library. There will be an empty disk image packaged that the data
    will mount to. Any interactions with the drive can be done via
    command line tools and the Finder interface.
Contact: Brandon Serna (bserna@usgs.gov)
Release Notes:
    Developed in 3.4 will run currently on osx installed 2.7
    Python 3.x urllib.request.urlretrieve
    Python 2.7.x urllib.urlretrieve
'''
import os
import urllib
import datetime
import time
import requests
import zipfile
from Tkinter import *
import threading

# custom files
from clean_disk_prep import remove_old_work, attach_image
from gui_test import chooser
from solr import fetch_solr_index
from additional_fileprocesses import create_vis, create_readme
from network import process_files


def main():
    example = []

    # Invoke gui menu
    #usr_kws = chooser()
    returned_info = chooser()
    usr_kws, get_id, file_size_get = returned_info
    print('Downloading files (limit: ' + file_size_get + ' this may take a while...')

    # Custom functions
    remove_old_work()
    attach_image()

    # Grab solr index
    second_lvl = fetch_solr_index()

    ############################################################################
    # Parse Solr and processing
    ############################################################################
    count = 0
    for i in second_lvl:
        try:
            grouping = second_lvl[count]
            idd = grouping['id']
            collection = grouping['collection_id']
            data_url = grouping['data_url']
            kws = grouping['keywords']

            # Process the Record ID portion
            # test record  coastalmap.marine.usgs.gov_metadata_eastcoast_midatl_block_island_sound_2012-002_296seddata_md.xml
            if get_id == idd:
                w_record = os.path.join(collection, idd)
                # URL Parsing
                for url in data_url:
                    # Send out for processing and download
                    process_files(url, collection, idd)
            if len(kws) < 1:
                pass
            else:
                # iterate through the keywords for matching
                for kw in usr_kws:
                    if kw in kws:
                        # print("ID: " + str(idd) + " Keyword: " + str(kw) + " URL: " + str(data_url))
                        w_record = os.path.join(collection, idd)
                        # URL Parsing
                        for url in data_url:
                            # Send out for processing and download
                            process_files(url, collection, idd, file_size_get)
                        # Also download the metadata
                        """
                        url_title = url.rpartition('/')[-1]
                        meta_url = os.path.join("http://usgs.ornl.gov/metadata/devcatalog/xml/", w_record)
                        start_files = os.path.join('sdc', os.path.join(collection, idd))
                        urllib.urlretrieve(meta_url, os.path.join(start_files, url))

                        #vis and readme
                        print_readme = create_readme(collection, idd)
                        w_record = os.path.join('sdc', w_record)
                        with open(os.path.join(w_record, 'readme.txt'), 'w') as wf:
                            wf.write(print_readme)
                            wf.close()

                        if data_url.endswith('.csv'):
                            print_html = create_vis(url_title, idd)
                            with open(url_title + '.html', 'w') as f:
                                f.write(print_html)
                                f.close()
                        """
                """
                for url in csvURL:
                    url_title = url.rpartition('/')[-1]
                    try:
                        response_check = requests.head(url)
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
                            if file_size < 500000:
                                try:
                                    # Collection folder exists
                                    if os.path.isdir(collection):
                                        # Record id folder exists
                                        # if os.path.isdir(os.path.join(collection, idd)):
                                        if os.path.isdir(os.path.join(collection, idd)):
                                            # w_record = os.path.join(collection, idd)
                                            w_record = os.path.join(collection, idd)
                                            full_file = os.path.join(w_record, url_title)
                                            # Download
                                            # urllib.request.urlretrieve(url, full_file)
                                            # Conversion for 2.7
                                            urllib.urlretrieve(url, full_file)
                                            # Also download the metadata
                                            meta_url = os.path.join("http://usgs.ornl.gov/metadata/devcatalog/xml/", w_record)
                                            # first = os.path.join(collection, idd)
                                            first = os.path.join(collection, idd)
                                            # urllib.request.urlretrieve(meta_url, os.path.join(first, idd))
                                            urllib.urlretrieve(meta_url, os.path.join(first, idd))
                                            # DOWNLOAD ZIP file
                                            for dataurlS in data_url:
                                                if dataurlS.endswith('.zip'):
                                                    print(dataurlS)
                                                    urllib.urlretrieve(dataurlS, os.path.join(w_record, dataurlS.rpartition('/')[-1]))
                                                    '''
                                                    zip_url_title = dataurlS.rpartition('/')[-1]
                                                    urllib.urlretrieve(dataurlS, os.path.join(first, idd))
                                                    with zipfile.ZipFile(dataurlS) as zf:
                                                        zf.extractall(os.path.join(first, idd))
                                                        zf.close()
                                                        print('Maybe a zipfile was processed...')
                                                    '''
                                            ############################################################################
                                            # Write readme
                                            ############################################################################
                                            print_readme = create_readme(collection, idd)
                                            with open(os.path.join(w_record, 'readme.txt'), 'w') as wf:
                                                wf.write(print_readme)
                                                wf.close()

                                            # Visualizations
                                            # viz_url = 'http://mercury.ornl.gov/USGSViz/vizUSGS?CSVUrl=http://usgs.ornl.gov/metadata/SDCdata/csv/' + url_title + '&ignoredLines=0&vizTitle=' + idd

                                            print_html = create_vis(url_title, idd)
                                            with open(full_file + '.html', 'w') as f:
                                                f.write(print_html)
                                                f.close()
                                        else:
                                            full_filename = os.path.join(collection, idd)

                                            # Make record_id folder
                                            os.makedirs(full_filename)

                                            # Join path for placement for the download
                                            with_id = os.path.join(full_filename, url_title)

                                            # Download
                                            # urllib.request.urlretrieve(url, with_id)
                                            urllib.urlretrieve(url, with_id)

                                            # Also download the metadata
                                            w_record = os.path.join(collection, idd)
                                            meta_url = os.path.join("http://usgs.ornl.gov/metadata/devcatalog/xml/", w_record)
                                            first = os.path.join(collection,idd)
                                            #urllib.request.urlretrieve(meta_url, os.path.join(first, idd))
                                            urllib.urlretrieve(meta_url, os.path.join(first, idd))

                                            # DOWNLOAD ZIP file
                                            for dataurlS in data_url:
                                                if dataurlS.endswith('.zip'):
                                                    print(dataurlS)
                                                    urllib.urlretrieve(dataurlS, os.path.join(w_record, dataurlS.rpartition('/')[-1]))
                                                    '''
                                                    zip_url_title = dataurlS.rpartition('/')[-1]
                                                    urllib.urlretrieve(dataurlS, os.path.join(first, idd))
                                                    with zipfile.ZipFile(dataurlS) as zf:
                                                        zf.extractall(os.path.join(first, idd))
                                                        zf.close()
                                                        print('Maybe a zipfile was processed...')
                                                    '''

                                            ############################################################################
                                            # Write readme
                                            ############################################################################
                                            print_readme = create_readme(collection, idd)
                                            with open(os.path.join(w_record, 'readme.txt'), 'w') as wf:
                                                wf.write(print_readme)
                                                wf.close()

                                            print_html = create_vis(url_title, idd)
                                            with open(with_id + '.html', 'w') as f:
                                                f.write(print_html)
                                                f.close()

                                    else:
                                        # When collection folder does not exist

                                        # Make collection folder
                                        os.makedirs(collection)

                                        # Make record folder
                                        full_filename = os.path.join(collection, idd)
                                        os.makedirs(full_filename)

                                        with_id = os.path.join(full_filename, url_title)
                                        # urllib.request.urlretrieve(url, with_id)
                                        urllib.urlretrieve(url, with_id)

                                        # Also download the metadata
                                        w_record = os.path.join(collection, idd)
                                        meta_url = os.path.join("http://usgs.ornl.gov/metadata/devcatalog/xml/", w_record)
                                        first = os.path.join(collection,idd)
                                        # urllib.request.urlretrieve(meta_url, os.path.join(first, idd))
                                        urllib.urlretrieve(meta_url, os.path.join(first, idd))

                                        # DOWNLOAD ZIP file
                                        for dataurlS in data_url:
                                            if dataurlS.endswith('.zip'):
                                                print(dataurlS)
                                                urllib.urlretrieve(dataurlS, os.path.join(w_record, dataurlS.rpartition('/')[-1]))
                                                '''
                                                    zip_url_title = dataurlS.rpartition('/')[-1]
                                                    urllib.urlretrieve(dataurlS, os.path.join(first, idd))
                                                    with zipfile.ZipFile(dataurlS) as zf:
                                                        zf.extractall(os.path.join(first, idd))
                                                        zf.close()
                                                        print('Maybe a zipfile was processed...')
                                                '''
                                        ############################################################################
                                        # Write readme
                                        ############################################################################
                                        print_readme = create_readme(collection, idd)
                                        with open(os.path.join(full_file, 'readme.txt'), 'w') as wf:
                                            wf.write(print_readme)
                                            wf.close()

                                        print_html = create_vis(url_title, idd)
                                        with open(with_id + '.html', 'w') as f:
                                            f.write(print_html)
                                            f.close()

                                    add_tolist = (idd, url_title, collection)
                                    example.append(add_tolist)
                                except Exception as e:
                                    pass
                                    # Add logging
                                    # print('Unable to retrieve:' + str(e))
                        except Exception as e:
                            # Need to add logging in future
                            # print(str(e))
                            pass
                """
        except Exception as e:
            # Add logging
            print('Main exception: ' + str(e))
            #pass
        count += 1

    ############################################################################
    # Write readme for collection
    ############################################################################

    date = datetime.datetime.now()
    date_formatted = date.strftime("%A %d. %B %Y")

    if os.path.isdir('sdc'):
        with open('sdc/readme.txt', 'w') as f:
            f.write('Science Data Catalog Drive \n\n')
            f.write('\nDate: ' + date_formatted)
            f.write('\nScience Data Catalog: http://www.data.usgs.gov')
            f.write('\nContact: sciencedatacatalog@usgs.gov')
            f.close()

    ############################################################################
    # Move files into the drive
    ############################################################################
    try:
        os.system("mv sdc/ /Volumes/SDC\ Drive/")
        #os.system("mv readme.txt /Volumes/SDC\ Drive/")
        os.system("rm *.zip")

    except Exception:
        print("Sorry error occurred when transferring files")

    print("DONE")

if __name__ == '__main__':
    main()
