from hashlib import md5

def hashlist(list_vals):
	m = md5()
	m.update('*'.join(list_vals))
	return m.hexdigest()

def hashdict(dict_vals, keys=None):
	m = md5()
	if keys is None:
		m.update('*'.join(dict_vals.values()))
	else:
		m.update('*'.join([dict_vals[key] for key in keys]))
	return m.hexdigest()
