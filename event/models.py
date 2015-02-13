from mongoengine import *
#from blog.settings import DBNAME

#connect(DBNAME)

class Event(Document):
    title = StringField(max_length=120, required=True)
    description = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
    date_start = DateTimeField()
    date_end = DateTimeField()
    #date_start = DateTimeField(required=True)
    #date_end = DateTimeField(required=True)