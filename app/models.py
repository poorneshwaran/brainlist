from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Brainstatus(models.Model):

	brainno    = models.CharField(max_length=30)
	seriesid   = models.CharField(max_length=30)
	dateofperf = models.DateTimeField()
	dateofimg  = models.DateTimeField()
	status     = models.IntegerField()
	lastupdate = models.DateTimeField()
	nextstep   = models.IntegerField()
	
