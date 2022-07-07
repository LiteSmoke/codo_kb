from django.db import models

# Create your models here.

class Video(models.Model):
    
    filename = models.CharField(max_length=255)
    filepath = models.CharField(max_length=512, blank=True)
    # creation_date = models.DateTimeField()
    meeting_name = models.CharField(max_length=512, blank=True)
    meeting_date = models.DateTimeField(blank=True, null=True)
    participants = models.CharField(max_length=512, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__ (self):
        return self.filename

class Tag(models.Model):

    name = models.CharField(max_length=512)
    type = models.ForeignKey('TagType', on_delete=models.CASCADE)

    def __str(self):
        return self.name

class TagType(models.Model):

    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name
     