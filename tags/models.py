from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tags(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TagItem(models.Model):
    # What tag applies to what object
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    # Type (Product, Category, etc)
    # ID of object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.tag.label
