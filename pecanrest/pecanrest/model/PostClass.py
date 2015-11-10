from mongoengine import *

class Post(Document):
	title = StringField(max_length=120, required=True)
	author = ReferenceField(User, reverse_delete_rule=CASCADE)
	tags = ListField(StringField(max_length=30))
	comments = ListField(EmbeddedDocumentField(Comment))
	meta = {'allow_inheritance': Ture}

class TestPost(Post):
	content = StringField()

class ImagePost(Post):
	content = StringField()

class LinkPost(Post):
	link_url = StringField()


