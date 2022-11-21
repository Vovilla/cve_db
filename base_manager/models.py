from django.db import models
from django.contrib.postgres.fields import ArrayField


class CVE(models.Model):
    name = models.CharField(max_length=500, default='CVE', primary_key=True)
    severity = models.CharField(max_length=500, default='Severity')
    url = models.CharField(max_length=500, default='URL')
    platforms = ArrayField(models.CharField(max_length=500, default='platform'), blank=True) 
    affected_junos = ArrayField(
                         ArrayField(models.CharField(max_length=500, default='junos'),
                                    blank = True,
                                    size=2
                         ),
                         blank = True      
                     ) 
    tags = ArrayField(models.CharField(max_length=500, default='tag'), blank=True) 
    
    def __str__(self):
        return self.name

class NetworkDevice(models.Model):
    cve = models.ManyToManyField(CVE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    # vendor = models.CharField(max_length=200)
    # os_type = models.CharField(max_length=200)
    # os_version = models.DateTimeField('date published')



