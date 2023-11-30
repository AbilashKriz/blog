from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    class Meta:
        app_label = 'djangoPartII'

    def __str__(self):
        return self.top_name
    
class webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    class Meta:
        app_label = 'djangoPartII'

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(webpage, on_delete=models.CASCADE)
    date = models.DateField()
    class Meta:
        app_label = 'djangoPartII'

    def __self__(self):
        return str(self.date)
    

class Friends(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    def __ste__(self):
        return self.first_name,self.last_name, self.email
    