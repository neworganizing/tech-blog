import csv

STREET_TYPES = ['pass','ln','way','pl','cir','cr','trl','wy','run','blvd','hwy','st','ct','dr','rd','ave']
APARTMENT_TYPES = ['trlr','spc','apt','unit','#']
DIRECTION_TYPES = ['s','se','sw','e','w','n','ne','nw']

fieldnames = ['id', 'county', 'house_number', 'apartment_number', 'street_direction', 'street_name', 'street_suffix', 'city', 'zip', 'precinct_name']
street_segment = {'id':'', 'county':'', 'house_number':'', 'apartment_number':'', 'street_direction':'', 'street_name':'', 'street_suffix':'', 'city':'', 'zip':'', 'precinct_name':''}

data = csv.reader(open("address_file.txt"))
err = csv.writer(open("address_file.err", "w"))
w = csv.DictWriter(open("address_file_clean.txt", "w"), fieldnames=fieldnames)

for row in data:

	street_segment = dict([(k, '') for (k, v) in street_segment.iteritems()])

	street_segment["id"] = row[0]
	street_segment["county"] = row[1]
	street_segment["city"] = row[7]
	street_segment["zip"] = row[9]
	street_segment["precinct_name"] = row[11]

	address = row[5].strip().split(" ")
	
	if len(address) > 8 or len(address) < 2:
		err.writerow(row)
		continue

	try:
		int(address[0])
	except:
		err.writerow(row)
		continue
	
	street_segment["house_number"] = address[0]

	if address[len(address)-1].isdigit():
		street_segment["apartment_number"] = address[len(address)-1]
		address.pop()
		while address[len(address)-1].lower() in APARTMENT_TYPES:
			address.pop()
	elif address[len(address)-1].startswith("#") and address[len(address)-1][1:].isdigit():
		street_segment["apartment_number"] = address[len(address)-1][1:]
		address.pop()
		while address[len(address)-1].lower() in APARTMENT_TYPES:
			address.pop()
	elif address[len(address)-2].lower() in APARTMENT_TYPES:
		err.writerow(row)
		continue
	elif address[len(address)-1].lower() not in STREET_TYPES and address[len(address)-2].lower() in STREET_TYPES and not address[len(address)-1].isdigit():
		err.writerow(row)
		continue

	if address[1].lower() in DIRECTION_TYPES:
		street_segment["street_direction"] = address[1]
		address.pop(1)
	if address[len(address)-1].lower() in STREET_TYPES:
		street_segment["street_suffix"] = address[len(address)-1]
		address.pop()
	street = ' '.join(address[1:])
	if street.replace("-","").replace("'","").replace(" ","").isalnum():
		street_segment["street_name"] = street
	else:
		print "character error"
		err.writerow(row)
		continue
	w.writerow(street_segment)
