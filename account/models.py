from mongoengine import *
import mongoengine.fields
#from blog.settings import DBNAME

#connect(DBNAME)

class Account(Document):
    name = StringField(max_length=50)
    username = StringField(max_length=30)
    password = StringField(max_length=30)
    email = EmailField(max_length=50)
