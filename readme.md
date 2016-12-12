# SDC Drive

A GUI application that collects user specified resources from the USGS Science Data Catalog (data.usgs.gov)

##### Structure

* one drive_beta.py: Main app file
* gui_test.py: gui-specific file
* clean_disk_prep.py: cleaning file
* solr.py: Interaction w/ solr index 
* additional_fileprocesses: readme.txt + visualizations 
* network.py

### Technology

Python 2.7 and 3.5 compatable

Python Requests library

Disk Images - FS aware to omit unused space while compressing other files

Apache Solr