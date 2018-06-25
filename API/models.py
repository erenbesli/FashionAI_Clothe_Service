from django.db import models

# Create your models here.


from mongoengine import Document, EmbeddedDocument, fields


class Clothe_Variant_Image(EmbeddedDocument):
    name = fields.StringField(required=False)
    value = fields.DynamicField(required=False)


class Clothe_Image(Document):
    image = fields.StringField(required=False)
    price = fields.StringField(required=False, null=True)
    gender = fields.StringField(required=False, null=True)
    image_class = fields.StringField(required=False, null=True)
    test_field = fields.StringField(required=False, null=True)
    test_list = fields.ListField(fields.EmbeddedDocumentField(Clothe_Variant_Image, required=False, null=True))
    test_list_2 = fields.ListField(required=False, null=True)


class Clothe_Image_Inferred(Document):
    bounding_box = fields.StringField(required=False)
    embedding_vector = fields.StringField(required=False, null=True)
    potential_combinations = fields.StringField(required=False, null=True)
    inferred_attributes = fields.StringField(required=False, null=True)


import json
from django.db import models
from django.utils import timezone


class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField()  # this stands for our crawled data
    date = models.DateTimeField(default=timezone.now)

    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id