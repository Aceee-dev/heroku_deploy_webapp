
from __future__ import unicode_literals

from django.db import models


class EoResults(models.Model):

 
    num_arr = models.CharField(max_length=4000)
    result1 = models.IntegerField()
    result2 = models.IntegerField()

    class Meta:
        db_table = 'eo_results'

    def __unicode__(self):
        return self.number