import avro.schema
import avro.datafile
import avro.io
import json
import os
import uuid
import pprint

def LoadAvsc(file_path, names=None):
	"""Load avsc file
	file_path: path to schema file
	names(optional): avro.schema.Names object
	"""

	file_text = open(file_path).read() 
	#print file_text
	json_data = json.loads(file_text)
	schema = avro.schema.make_avsc_object(json_data, names) 
	return schema 

filepaths = ['entrance.avsc.json', "feature.avsc.json"]
#types = ['entrystatus.avsc.json', 'entryownership.avsc.json', 'entrancenegotiation.avsc.json', 'entranceformation.avsc.json', 'entrancecharacteristics.avsc.json', 'entrancelocation.avsc.json', 'entrancehydrology.avsc.json', 'entrancehazards.avsc.json', 'entrancetype.avsc.json']
known_schemas = avro.schema.Names()

for fpath in os.listdir('primitives'):
	if fpath.endswith('.avsc.json'):
		print "Found Primitive: %s" % fpath
		types_schema = LoadAvsc("primitives/%s" % fpath, known_schemas)

types_schema = LoadAvsc("entrance.avsc.json", known_schemas)
param_schema = LoadAvsc("feature.avsc.json", known_schemas)

print param_schema

rec_writer = avro.io.DatumWriter(param_schema)
df_writer = avro.datafile.DataFileWriter(open("test.avro", 'wb'), rec_writer, writers_schema=param_schema)
test_obj = {
	"uuid": str(uuid.uuid4()),
	"name": "Sample Cave",
	"code": "SAMPLE",
	"length": 5280,
	"depth": 5280,
	"entrances": None,
	"discovered": 1444840530,
	"discovered_by" :"Joe Caver",
	"created": 1444840530,
	"created_by": "Joe Caver",
	"last_modified": 1444840530,
	"last_modified_by": "Joe Caver",
	"narrative": "a cool cave",
	"maps": [{"uuid": str(uuid.uuid4()), "title": "test", "description": "", "filename": "poia.pdf", "mimetype": "pdf", "image_data": open("poia.pdf",'r').read()}],
	"photos": [None]
}
df_writer.append(test_obj)
df_writer.close()


#for filepath in filepaths:
#	schema = avro.schema.parse(open(filepath).read())