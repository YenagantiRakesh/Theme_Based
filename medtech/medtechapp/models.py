from django.db import models

# Create your models here.
class Solutions(models.Model):
    disease=models.CharField(max_length=200)
    ingredients=models.CharField(max_length=300)
    pic1=models.CharField(max_length=1000)
    pic2=models.CharField(max_length=1000)
    pic3=models.CharField(max_length=1000)
    sol1=models.CharField(max_length=300)
    sol2=models.CharField(max_length=300)
    sol3=models.CharField(max_length=300)
    

    def __str__(self):
        return self.disease+' - '+self.ingredients



class NewEntryTable(models.Model):
    fname=models.CharField(default='',max_length=100)
    lname=models.CharField(default='',max_length=100)
    email=models.CharField(default='',max_length=100)
    contact=models.CharField(default='',max_length=100)
    hname=models.CharField(default='',max_length=100)

    def __str__(self):
        return self.fname + ' ' + self.lname


class DonationTable(models.Model):
    user=models.CharField(default='',max_length=100)
    gender=models.CharField(default='',max_length=100)
    birth=models.CharField(default='',max_length=100)
    address=models.CharField(default='',max_length=100)
    mobile_no=models.CharField(default='',max_length=100)
    pincode=models.CharField(default='',max_length=100)
    organs=models.CharField(default='',max_length=100)
    blood_group=models.CharField(default='',max_length=100)
    myfile=models.CharField(default='',max_length=100)
    # myfile = models.ImageField(upload_to='img')


    def __str__(self):
        return self.user + ''+self.address
    

class Hospital(models.Model):
    hospitalname=models.CharField(max_length=100)
    token=models.IntegerField()
    def __str__(self):
        return self.hospitalname + ' ' + str(self.token)

