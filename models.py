from django.db import models

# Create your models here.
class About(models.Model):
    about_title = models.CharField(max_length=200)
    about_content = models.TextField()
    about_published = models.DateTimeField("date published")

    def __str__(self):
        return self.about_title
'''
class Demo(models.Model):
    demo_content = models.TextField()
'''
