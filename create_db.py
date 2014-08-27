import couchdb
couch = couchdb.Server()  # make sure the server is running

print
print ' loading ', couch
print 

for database in couch:
    print '     ',database
print
    
db = raw_input('enter name of data base to access or create: ')
    
if db in couch:
    active_db = couch[db]
    print
    print 'There are',len(active_db),'documents in',active_db
    for id in active_db:
        print
        for key in sorted(active_db[id].keys()):
            print key
else:
    really = raw_input('so you want to create a new db {} ? '.format(db))
    if really =="yes" or really=="y":
        couch.create(db)
        print 'database',db,'created'

        for database in couch:
            print '     ',database
            print


