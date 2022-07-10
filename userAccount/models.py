from django.db import models

# Create your models here.


class UserMessageModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=150)
    message = models.TextField(max_length=225)

    class Meta:
        db_table= 'user_message'
