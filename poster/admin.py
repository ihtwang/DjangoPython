# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from poster import models

# Register your models here.
admin.site.register([models.Tweet,models.Comment])