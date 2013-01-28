def hashlist(list_vals):
	return hash(tuple(list_vals))

def hashdict(dict_vals, keys=None):
	if keys is None:
		return hash(tuple(dict_vals.values()))
	return hash(tuple([dict_vals[key] for key in keys]))
