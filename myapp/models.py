from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='signup', null=True, blank=True)
    Full_Name = models.CharField(max_length=100, default='Default fullname')
    Email = models.EmailField(default='default@example.com')
    Username = models.CharField(max_length=100, default='Default username')
    Password = models.CharField(max_length=100, default='Default password')


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Schoolname = models.CharField(max_length=100, default='Default schoolname')
    Passoutyear1 = models.IntegerField(null=True, blank=True)
    Score1 = models.IntegerField(null=True, blank=True)
    Ug = models.CharField(max_length=100, default='Default ug')
    Passoutyear2 = models.IntegerField(null=True, blank=True)
    Score2 = models.IntegerField(null=True, blank=True)
    Pg = models.CharField(max_length=100, default='Default pg')
    Passoutyear3 = models.IntegerField(null=True, blank=True)
    Score3 = models.IntegerField(null=True, blank=True)


class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=10, default='Default gender')
    address = models.CharField(max_length=255, default='Default address')
    phone = models.IntegerField(null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)


class Professional(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Aadharnumber = models.CharField(max_length=12, default='Default aadhaar')
    Pannumber = models.CharField(max_length=10, default='Default pan')
    Passportnumber = models.CharField(max_length=10, default='Default passport')
    Licencenumber = models.CharField(max_length=16, default='Default license')
    Electionid = models.CharField(max_length=16, default='Default election')


class Medical(models.Model):
    THYROID_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    ALLERGY_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    DIABETIC_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]

    ASTHMA_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]

    BP_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]

    CHOLESTROL_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    thyroid = models.CharField(max_length=10, null=False, blank=False)
    asthma = models.CharField(max_length=10, null=False, blank=False)
    allergy = models.CharField(max_length=10, null=False, blank=False)
    diabetic = models.CharField(max_length=10, null=False, blank=False)
    bp = models.CharField(max_length=10, null=False, blank=False)
    cholestrol = models.CharField(max_length=10, null=False, blank=False)


class Financial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    loan1 = models.CharField(max_length=100, default='Default loan')
    amount1 = models.CharField(max_length=100, default='Default amount')
    payment1 = models.CharField(max_length=100, default='Default payment')
    loan2 = models.CharField(max_length=100, default='Default loan')
    amount2 = models.CharField(max_length=100, default='Default amount')
    payment2 = models.CharField(max_length=100, default='Default payment')
    loan3 = models.CharField(max_length=100, default='Default loan')
    amount3 = models.CharField(max_length=100, default='Default amount')
    payment3 = models.CharField(max_length=100, default='Default payment')



class contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Message= models.CharField(max_length=100)


    def __str__(self):
        return self.Name

