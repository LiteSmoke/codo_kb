from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class TsRecord(models.Model):

    date = models.DateField(null=False, blank = False)
    project = models.ForeignKey('Project', on_delete = models.CASCADE)
    activity = models.CharField(null = False, blank = False, max_length = 512)
    fact_hours = models.FloatField(null = False, blank = False)
    # accepted_hours = models.IntegerField(null = True, blank = True)
    person = models.ForeignKey(User, on_delete = models.CASCADE)
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.project) + ' - ' + self.activity
    
class Project(models.Model):

    name = models.CharField(null = False, blank = False, max_length = 64)

    def __str__(self):
        return self.name

def user_get_name(self):
    return self.first_name + " " + self.last_name

User.add_to_class('__str__', user_get_name)

# class Person(User):

#     def __str__(self):
#         return self.first_name + " " + self.last_name

#     class Meta:
#         proxy = True
