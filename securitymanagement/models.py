from django.db import models

# Create your models here.

#Security page
class visitor(models.Model):
    visitorName = models.TextField(max_length=200)
    visitorIc = models.CharField(max_length=200,primary_key=True)
    visitorPhone = models.CharField (max_length=200)
    visitorDate = models.CharField (max_length=200)

class securitydata(models.Model):
    securityID = models.CharField(max_length=10, primary_key=True)
    securityName = models.TextField(max_length=200)
    securityIC = models.CharField(max_length=200)
    securityNophone = models.CharField(max_length=200)

class securityIncident(models.Model):
    incidentID = models.CharField(max_length=200,primary_key=True)
    incidentDate = models.CharField(max_length=200)
    incidentLoc = models.TextField(max_length=200)
    incidentDesc = models.TextField(max_length=200)

class securityShift(models.Model):
    securityID = models.ForeignKey(securitydata, on_delete = models.CASCADE)
    shiftDate = models.CharField(max_length=200)
    startTime = models.CharField(max_length=200)
    endTime = models.CharField(max_length=200)
    Shiftdesc = models.TextField(max_length=200)