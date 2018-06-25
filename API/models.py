from django.db import models

# Create your models here.


from mongoengine import Document, EmbeddedDocument, fields


class clothe_images(Document):
    category = fields.StringField(required=False)
    brand = fields.StringField(required=False)
    product_code = fields.StringField(required=False)
    price = fields.IntField(required=False)
    image_path = fields.StringField(required=False)
    size_fit_information = fields.StringField(required=False)
    editors_notes = fields.StringField(required=False)


class embedded_clothe_images(EmbeddedDocument):
    category = fields.StringField(required=False)
    brand = fields.StringField(required=False)
    product_code = fields.StringField(required=False)
    price = fields.IntField(required=False)
    image_path = fields.StringField(required=False)
    size_fit_information = fields.StringField(required=False)
    editors_notes = fields.StringField(required=False)


class list_Of_clothe_images(Document):
     products = fields.EmbeddedDocumentListField(embedded_clothe_images)
