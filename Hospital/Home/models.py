from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField(max_length=250)
    dep_img = models.ImageField(upload_to='doepartments')

     
    def __str__(self):
        return self.dep_name
    
class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name= models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_img = models.ImageField(upload_to='doctors')

    def __str__(self):
        return self.doc_name

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone =
    p_email =
    dep_name =
    doc_name =
    booking_date =