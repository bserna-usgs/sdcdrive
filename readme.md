# Science Data Catalog Drive

A graphical user interface application that collects user specified resources from the U.S. Geological Survey's Science Data Catalog (data.usgs.gov). This project is inspired by the DataONE ONEDrive application; alterations in the design were made in order for the application to be ran by standard user accounts. The data intended for current exploration is science metadata with attached tabular and GIS data organized by internal keywords. For more information or an OSX application bundle please contact us. 

##### App Structure

```sh
sdc_onedrive/
├── app
│   ├── additional_fileprocesses.py
│   ├── clean_disk_prep.py
│   ├── collect_shape.py
│   ├── gui_test.py
│   ├── keywords.txt
│   ├── network.py
│   ├── onedrive.py
│   ├── sdc_beta.dmg
│   ├── solr.py
│   └── usgs-sdc_template_wCSS.html
├── tests/
├── readme.md
```

### Developer Resources

Python 2.7 and 3.5 compatable

Python Requests library

Disk Images - FS aware to omit unused space while compressing other files

Apache Solr

### Contacts

Brandon Serna - USGS (bserna@usgs.gov)

Ranjeet Devarakonda - ORNL ()

Mike Frame - USGS ()

### License 

### Other 

Resources:

Science Data Catalog: data.usgs.gov

Official repository: https://my.usgs.gov/bitbucket/projects/SDC/repos/sdcdrive/browse

DataONE: https://www.dataone.org/

DataONE ONEDrive: http://pythonhosted.org/dataone.onedrive/

**This software is preliminary and for research/review purposes only. It does NOT currently represent an official release or product**