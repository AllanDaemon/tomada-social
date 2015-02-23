from mongoengine import *
import mongoengine.fields

class Account(Document):
    PERFIL_CHOICES = (
        (u'N', u'Normal'),
        (u'M', u'Moderador'),
        (u'R', u'Root'),
    )

    name = StringField(max_length=50)
    username = StringField(max_length=30)
    password = StringField(max_length=30)
    email = EmailField(max_length=50)
    perfil = StringField(max_length=1, choices=PERFIL_CHOICES)
    event_going = ListField(GenericReferenceField())
    event_maybe = ListField(GenericReferenceField())
    event_invite = ListField(GenericReferenceField())

