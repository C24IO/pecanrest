from mongoengine import *

class CommentClass(EmbeddedDocument):
	content = StringField()
	name = StringField(max_length=120)
