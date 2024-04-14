import csv
from datetime import datetime
import xml.etree.ElementTree as ET

def extract_date_time(kml_file, csv_file):
    tree = ET.parse(kml_file)
    root = tree.getroot()

    timestamps = []
    
    for when in root.iter('{http://www.opengis.net/kml/2.2}when'):
        timestamp = datetime.strptime(when.text, '%Y-%m-%dT%H:%M:%S.%fZ')
        date_time = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        timestamps.append(date_time)

    #write timestamps 
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp'])
        writer.writerows(zip(timestamps))

    print(f"Timestamps written to {csv_file} successfully!")



#files
kml_file = ''
csv_file = ''
extract_date_time(kml_file, csv_file)
