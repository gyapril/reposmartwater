from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username = models.CharField(max_length=100, blank=True, null=True)
    Password = models.CharField(max_length=100, blank=True, null=True)
    Type = models.CharField(max_length=100, blank=True, null=True)

class UserTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name =  models.CharField(max_length=100, blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True) 
    Gender = models.CharField(max_length=10, blank=True, null=True)
    Email = models.CharField(max_length=50,  blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)


class ConnectionTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    ConnectionNo = models.IntegerField(blank=True, null=True)
    Report = models.FileField(blank=True, null=True)
    Date = models.DateField(blank=True, null=True)
    status=models.CharField(max_length=100,null=True,blank=True)


class ComplaintTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Complaint = models.CharField(max_length=100,blank=True, null=True)
    Date = models.DateField(blank=True, null=True)
    Reply = models.CharField(max_length=100,blank=True, null=True)

class PaymentTable(models.Model):
    CONNECTION = models.ForeignKey(ConnectionTable, on_delete=models.CASCADE)
    Contact = models.BigIntegerField(blank=True, null=True)
    PaymentStatus = models.CharField(max_length=30,blank=True, null=True)
    DueDate = models.DateField(blank=True, null=True)


class WaterQualityTable(models.Model):
    QualityStatus = models.CharField(max_length=30,blank=True, null=True)
     
class AreaTable(models.Model):
    Areas = models.CharField(max_length=30, blank=True, null=True)
    Description = models.CharField(max_length=30,blank=True, null=True)
    

   

class NotificationTable(models.Model):
    Notification = models.CharField(max_length=30,blank=True, null=True)
    Date = models.DateField(blank=True, null=True)

class SubAdminTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)
    Name =  models.CharField(max_length=100, blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True) 
    Gender = models.CharField(max_length=10, blank=True, null=True)
    Email = models.CharField(max_length=50,  blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Actions = models.CharField(blank=True, null=True, max_length=100)
    
class ReaderTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)
    Name =  models.CharField(max_length=100, blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True) 
    Gender = models.CharField(max_length=10, blank=True, null=True)
    Email = models.CharField(max_length=50,  blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Area=models.ForeignKey(AreaTable,on_delete=models.CASCADE,null=True,blank=True)

