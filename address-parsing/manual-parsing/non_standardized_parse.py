from csv import DictReader, DictWriter
from hashlib import md5

def hash_list(vals,fields):
	m = md5()
	for f in fields:
		m.update(vals[f])
	return m.hexdigest()

add_hashes = set([])
precinct_data = {}
fields = ['county','house_number','apartment_number','street_name','predirection','postdirection','precinct_code','suffix','city','state','zip','citycode','ward','precinct_id']
DIRS = ['N','W','E','S','NW','NE','SW','SE']
SUFFIXES = ['DR','CIR','ST','PKWY','AVE','LN','PL','CT','TRL','PASS','BLVD','COURT','DRIVE','CIRCLE','LANE','LOOP','STREET','AVENUE','TERRACE','ROAD']
count = 0
good_count = 0
nonerror_count = 0
precinct_count = 0
with open('addresses.txt','r') as r, open('ss.txt','w') as w:
	reader = DictReader(r)
	writer = DictWriter(w,fieldnames=fields)
	writer.writeheader()
	for row in reader:
		count += 1
		add_array = row['Address'].split()
		output = {'county':row['CountyCode'],
				'house_number':'',
				'apartment_number':'',
				'street_name':'',
				'predirection':'',
				'postdirection':'',
				'suffix':'',
				'city':row['City'].strip(),
				'state':'SD',
				'zip':row['Zip'].strip(),
				'precinct_code':row['Precinct'].strip(),
				'citycode':row['CityTwn'].strip(),
				'ward':row['Ward'].strip()}
		if len(add_array) == 0:
			continue
		try:
			output['house_number'] = str(int(add_array.pop(0)))
		except:
			continue
		for i in range(len(add_array)):
			if add_array[i] == 'POB':
				add_array.pop(i)
				add_array.pop(i)
				break
			if add_array[i] == 'PO' and add_array[i+1] == 'BOX':
				add_array.pop(i)
				add_array.pop(i)
				add_array.pop(i)
				break
		if not add_array:
			continue
		if add_array[0] in DIRS:
			output['predirection'] = add_array.pop(0)
		if 'HWY' not in add_array and 'HIGHWAY' not in add_array:
			for i in range(len(add_array)):
				if add_array[i] in ['APT','UNIT','LOT','PMB'] and i+1 < len(add_array):
					add_array.pop(i)
					output['apartment_number'] = add_array.pop(i).replace('#','')
					break
				if add_array[i].find('#') >= 0:
					if len(add_array[i]) > 1:
						output['apartment_number'] = add_array.pop(i).replace('#','')
					elif i+1 == len(add_array) and len(add_array[i]) == 1:
						output['apartment_number'] = add_array.pop(i).replace('#','')
					else:
						add_array.pop(i)
						output['apartment_number'] = add_array.pop(i).replace('#','')
					break
				if i == len(add_array)-1 and add_array[i].isdigit() and len(add_array) > 1:
					output['apartment_number'] = add_array.pop(i)
					break
		if len(add_array) > 1 and add_array[len(add_array)-1] in DIRS:
			output['postdirection'] = add_array.pop(len(add_array)-1)
		if len(add_array) > 1 and add_array[len(add_array)-1] in SUFFIXES:
			output['suffix'] = add_array.pop(len(add_array)-1)
		output['street_name'] = ' '.join(' '.join(add_array).replace('#','').split())
		precinct_hash = output['county']+'*'+output['precinct_code']
		if precinct_hash in precinct_data:
			precinct_data[precinct_hash]['vf_precinct_count'] += 1
			output['precinct_id'] = precinct_data[precinct_hash]['vf_precinct_id']
		else:
			precinct_count += 1
			precinct_data[precinct_hash] = {'vf_precinct_id':'22'+str(precinct_count),
							'vf_precinct_county':output['county'],
							'vf_precinct_city':output['city'],
							'vf_precinct_zip':output['zip'],
							'vf_precinct_ward':output['ward'],
							'vf_precinct_name':output['precinct_code'],
							'vf_precinct_code':output['precinct_code'],
							'vf_precinct_count':1}
			output['precinct_id'] = '22'+str(precinct_count)
		hash_val = hash_list(output,fields)
		nonerror_count += 1
		if hash_val in add_hashes:
			continue
		add_hashes.add(hash_val)
		writer.writerow(output)
		good_count += 1
