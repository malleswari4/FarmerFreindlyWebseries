from django.db import models

# Create your models here.
class logindb(models.Model):
    email=models.EmailField(null=False)
    upass=models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.email+""+self.password

class registerdb(models.Model):
    name=models.CharField(max_length=50,null=False)
    mail=models.EmailField(null=False)
    land=models.IntegerField(null=False)
    phone=models.IntegerField(null=False)
    regpass=models.CharField(max_length=50)
    def __str__(self):
        return self.name+""+self.email

class userdb(models.Model):
    uname=models.CharField(max_length=50,null=False)
    umail=models.EmailField(null=False)
    phone=models.IntegerField(null=False)

    def __str__(self):
        return self.uname+""+self.umail+""+self.phone