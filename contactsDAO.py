import string

#https://github.com/veritas7/MongoDB-apps

class contactsDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
		def __init__(self, database):
				self.db = database
				self.listMembers = database.listMembers
				
#This function will handle the finding of names
		def find_names(self):
				l=[]
				for each_name in self.listMembers.find():
						l.append({'Name':each_name['Name'], 'CellPhone':each_name['CellPhone']})
						
				return l
				
#This function will handle the insertion of names
		def insert_name(self,newname,newcellphone):
				newname={'Name':newname,'CellPhone':newcellphone}
				self.listMembers.insert(newname)
				