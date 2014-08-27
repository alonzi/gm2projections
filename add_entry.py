import couchdb
import schema

couch = couchdb.Server()  # make sure the server is running
db = couch['gm2']

print len(db)

document = {}

for item in schema.fields:
    document[item]=raw_input(" enter  {}: ".format(item))

doc_id, doc_rev = db.save(document)

print len(db)

