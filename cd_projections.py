import couchdb
from pylab import *

couch = couchdb.Server()  # make sure the server is running
db = couch['gm2']

axis=[]
data=[]

for row in db.view('prototype/date_projected_cd_2'):
    axis.append(row.key[:4])
    data.append(row.value[2:6])

print axis
print data
plot(axis,data)
show()
