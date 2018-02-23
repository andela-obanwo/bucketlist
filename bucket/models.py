# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ListItems(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BucketList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Users)
    list_items = models.ManyToManyField(ListItems, related_name='bucket_list')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "{}-{}".format(self.user.name, self.name)



