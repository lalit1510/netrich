from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Course(models.Model):
    name=models.CharField(max_length=400)
    def __str__(self):
        return self.name


class Student(models.Model):
    CHOICES = (
        ('Part-Payment', 'Part-Payment'),
        ('full-Payment', 'Full-Payment')
    )
    CHOICES1 = (
        ('Enquiary', 'Enquiary'),
        ('Registered', 'Register')
    )
    PAYMENT_CHOICES=(
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online')
    )
    name=models.CharField(max_length=256)
    email=models.CharField(max_length=256,unique=True)
    mobile = models.CharField(max_length=10,unique=True, validators=[RegexValidator(regex='^[6-9]\d{9}$', message='Length has to be 10', code='Invalid number')])
    course=models.ForeignKey(Course,related_name='student_course',on_delete=models.CASCADE)
    city = models.CharField(max_length=256, blank=True, null=True)
    college = models.CharField(max_length=256, blank=True, null=True)
    student_status=models.CharField(max_length=25,choices=CHOICES1)
    enquiary_date=models.DateField()

    fees=models.CharField(max_length=6,blank=True,null=True,validators=[RegexValidator(regex='^\d{4,5}$', message='Fees should be numeric value', code='Invalid number')])
    mode_of_payment=models.CharField(max_length=20,choices=PAYMENT_CHOICES,blank=True,null=True)
    payment_status=models.CharField(max_length=100,choices=CHOICES,blank=True,null=True)
    remaining_fees=models.CharField(max_length=5,blank=True,null=True)
    fees_date=models.DateField(blank=True,null=True)
    remaining_fees_date = models.DateField(max_length=50, blank=True, null=True)
    address=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-fees_date','-enquiary_date')



