from django.db import models

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class CareerApplication(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    plf = models.TextField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
   
    education_level = models.CharField(max_length=100)
    experience = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.first_name

# Create your models here.
