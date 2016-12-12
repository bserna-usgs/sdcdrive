'''
Visualizations
This file creates the csv viewer in an html page
'''
import datetime


def create_vis(url_title, idd):
    viz_url = 'http://mercury.ornl.gov/USGSViz/vizUSGS?CSVUrl=http://usgs.ornl.gov/metadata/SDCdata/csv/' + url_title + '&ignoredLines=0&vizTitle=' + idd

    generate_markup_head = """<html><body><body><div style="background: #000 url(http://www.usgs.gov/images/headers/blue_black.jpg) 178px 0px no-repeat; font: 14px Verdana, Arial,
    Helvetica, sans-serif; width: 100%; height: 5.14em; min-height:72px;"><div id="usgsidentifier" style="float: left;"><a href="http://www.usgs.gov/"><img src="http://www.usgs.gov/images/header_graphic_usgsIdentifier_white.jpg" alt="USGS - science for a changing world" title="U.S. Geological Survey Home Page" height="72
    " width="178"></a></div><div style="color: white;" id="usgsccsabox"><div style="float:right; background-color: black; min-height: 72px; font: bold 1em/1.3em Verdana, Arial, Helvetica, sans-serif; color: #ffffff; margin-left:4px; text-decoration: none;">
    <br><a style="color:white;" href="http://www.usgs.gov/">USGS Home</a>
    <br><a style="color: white;" onmousedown="_sendEvent('Outbound','answers.usgs.gov','/cgi-bin/gsanswers',0);" href="http://answers.usgs.gov/cgi-bin/gsanswers?tmplt=2">Contact USGS</a>
    <br><a style="color:white;" onmousedown="_sendEvent('Outbound','search.usgs.gov','/',0);" href="http://search.usgs.gov/">Search USGS</a><br></div></div></div>
    <div style="background-color: #5b5b5b; color: white; font: bold 1.3em Verdana, Arial, Helvetica, sans-serif; font-size:16px; ">U.S. Geological Survey Science Data Catalog</div>"""

    generate_iframe = '<iframe style="height: 700px ; width: 100% ;" src="' + viz_url

    generate_error = '"><p>Sorry this browser doesnt support iframes</p>'

    generate_markup_foot = """</iframe><div style="font-family: Verdana, Arial, Helvetica; font-size: 13;"><p style="background-color: #666666; padding: 4px; margin:0;;" id="usgsfooterbar"><a onmousedown="_sendEvent('Outbound','www.usgs.gov','/laws/accessibility.html',0);" style="color:white;" href="http://www.usgs.gov/laws/accessibility.html" title="Accessibility Policy (Section 508)">Accessibility</a> <a onmousedown="_sendEvent('Outbound','www.usgs.gov','/foia/',0);" style="color:white;" href="http://www.usgs.gov/foia/" title="Freedom of Information Act">FOIA</a>
<a onmousedown="_sendEvent('Outbound','www.usgs.gov','/laws/privacy.html',0);" href="http://www.usgs.gov/laws/privacy.html" style="color:white" title="Privacy policies of the U.S. Geological Survey.">Privacy</a>
<a onmousedown="_sendEvent('Outbound','www.usgs.gov','/laws/policies_notices.html',0);" href="http://www.usgs.gov/laws/policies_notices.html" style="color:white" title="Policies and notices that govern information posted on USGS Web sites.">Policies
                                and Notices</a></p><p id="usgsfootertext" style="float:right"><a onmousedown="_sendEvent('Outbound','www.takepride.gov','/',0);" href="http://www.takepride.gov/"><img src="http://data.usgs.gov/datacatalog/images/footer_graphic_takePride.jpg" alt="Take Pride in America logo" title="Take Pride in America Home Page" height="58" width="60"></a> <a onmousedown="_sendEvent('Outbound','www.usa.gov','/',0);" href="http://usa.gov/"><img src="http://data.usgs.gov/datacatalog/images/footer_graphic_usagov.jpg" alt="USA.gov logo" title="USAGov: Government Made Easy" height="26" width="90"></a>
<div style:"float:left"> <a onmousedown="_sendEvent('Outbound','www.doi.gov','/',0);" href="http://www.doi.gov/">U.S. Department of the Interior</a> | <a onmousedown="_sendEvent('Outbound','www.usgs.gov','/',0);" href="http://www.usgs.gov/">U.S. Geological Survey</a><br> Page
                        Contact Information: <a onmousedown="_sendEvent('Outbound MailTo','csas@usgs.gov','',0);" href="mailto:csas@usgs.gov">ASK CSAS&amp;L</a><br>
                        Page Last Modified: Tomorrow </p></div></div></body></html>"""

    return generate_markup_head + generate_iframe + generate_error + generate_markup_foot


# readme
def create_readme(collection, idd):
    date = datetime.datetime.now()
    date_formatted = date.strftime("%A %d. %B %Y")

    header = "Science Data Catalog Drive \n\n"
    colrec = "Collection: " + collection + "\nRecord id: " + idd
    date_print = "\nDate: " + date_formatted

    return header + colrec + date_print
