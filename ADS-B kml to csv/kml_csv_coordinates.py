import csv

def extract_altitude(kml_file, csv_file):
    with open(kml_file, 'r') as file:
        reader = file.readlines()

    coordinates = []

    for line in reader:
        if '<gx:coord' in line:
            coord = line.split('>')[1].split('</gx:coord')[0].strip().split()
            coordinates.append(coord)
    #write coords 
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Latitude', 'Longitude', 'Altitude'])

        for coord in coordinates:
            lat, lon, altitude = coord
            writer.writerow([lat, lon, altitude])


#files
kml_file = ''
csv_file = ''
extract_altitude(kml_file, csv_file)
