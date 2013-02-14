from argparse import ArgumentParser

#Voter File parsing example
usage='Input state and optional county values'
description='Accepts input to process voter files'
parser = ArgumentParser(usage=usage,description=description)

parser.add_argument('-s','--state',action='store',dest='state',
    help='State value to process',required=True)
parser.add_argument('-c','--county',action='store',dest='county',
    help='Optional county in state process')

args = parser.parse_args()
loc_data = {'state':args.state,'county':args.county}

#DB creation example
description='create database from schema'
parser = ArgumentParser(description=description)

parser.add_argument('-d', action='store', dest='db_type',
    help='database type, valid types are: sqlite, mysql, postgres')

parser.add_argument('-u', action='store', dest='username',
    help='username to access the database')
	
parser.add_argument('-n', action='store', dest='db_name',
    help='database name the data is stored in')

parser.add_argument('-host', action='store', dest='host',
    help='database host address, database file location using sqlite')

