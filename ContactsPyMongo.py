import bottle
import pymongo
import contactsDAO

#https://github.com/veritas7/MongoDB-apps

@bottle.route('/')
def contacts_index():
		listMembers_list = contacts.find_names()
		return bottle.template('index', dict(listMembers = listMembers_list))
		
@bottle.route('/newcontact', method='POST')
def insert_newcontact():
		Name = bottle.request.forms.get("Name")
		CellPhone = bottle.request.forms.get("CellPhone")
		contacts.insert_name(Name, CellPhone)
		bottle.redirect('/')
		
#Connection String
connection_string = "mongodb://localhost"
#Let PyMongo make friends with the connection string
connection = pymongo.MongoClient(connection_string)
#Set the database context to contactList (make this using the 'mongo' command shell)
database = connection.contactList
#Refer the DAO to the database context
contacts = contactsDAO.contactsDAO(database)

bottle.debug(True)
bottle.run(host='localhost', port=8082)