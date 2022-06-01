from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(default=0)

    def __str__(self):
         return self.job_title
