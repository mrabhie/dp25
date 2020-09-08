from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,unique=True,blank=False)

    def __str__(self):
        return self.topic_name
    
class WebPage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,blank=False)
    url=models.URLField(max_length=100,blank=False,unique=True)

    def __str__(self):
        return self.name

class AccessDetails(models.Model):
    webpage=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    datetime=models.DateTimeField()

    def __str__(self):
        return self.datetime
    
    