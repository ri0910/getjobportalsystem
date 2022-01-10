from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Job_seeker(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=15,null=True)
    def _str_(self):
        return self.user.username
class Company(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    companyname=models.CharField(max_length=100,null=True)
    website=models.CharField(max_length=30,null=True)
    type=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=20,null=True)
    def _str_(self):
        return self.user.username
class Job(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    job_role=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    salary=models.FloatField(max_length=20)
    description=models.CharField(max_length=300)
    location=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
    required_skills=models.CharField(max_length=100)
    creation_date=models.DateField()
    def _str_(self):
        return self.job_role
class Apply(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    job_seeker=models.ForeignKey(Job_seeker,on_delete=models.CASCADE)
    resume=models.FileField(null=True)
    apply_date=models.DateField()
    def _str_(self):
        return self.id