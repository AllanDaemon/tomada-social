from mongoengine import *
import mongoengine.fields
#from blog.settings import DBNAME

#connect(DBNAME)

class Event(Document):
    title = StringField(max_length=120, required=True)
    description = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
    date_start = DateTimeField()
    date_end = DateTimeField()
    location = GeoPointField()
    image = ImageField()
    user = GenericReferenceField()
    user_going = ListField(GenericReferenceField())
    user_maybe = ListField(GenericReferenceField())
    user_invite = ListField(GenericReferenceField())
    #date_start = DateTimeField(required=True)
    #date_end = DateTimeField(required=True)