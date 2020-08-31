from django.db import models
import os
# Create your models here.
class home_content(models.Model):
    title = models.CharField(max_length= 50, null=True, unique=True)
    description = models.TextField(max_length=500, null=True)
    pic = models.ImageField(upload_to="static/img/home")

    sectionTitle = models.CharField(max_length=50, null=True)
    sectionDescription = models.TextField(max_length= 500, null=True)

    def __str__(self):
        return self.title

# class pictures(models.Model):
# logo = models.ImageField()


class about_content(models.Model):
    title = models.CharField(max_length=50, null=True, unique=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

# class photos(models.Model):


class portfolio_content(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bio = models.TextField(max_length = 300)
    pic = models.ImageField(upload_to= "static/img/portfolio", null=True)

    def __str__(self):
        return self.name


class service_content(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=5000, null=True)
    #pic = models.ImageField(upload_to="static/img/service", null=True)

    def __str__(self):
        return self.title


class our_work_content(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class header(models.Model):
    company_name = models.CharField(max_length=50, unique=True)
    pic = models.ImageField(upload_to='static/img/logo', null=True)
    welcome = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.company_name


class contact(models.Model):
    address = models.CharField(max_length=100, null=True, unique=False)
    phone = models.TextField(null=True, unique=False)
    email = models.CharField(max_length= 25, null=True, unique=False)

    def __str__(self):
        return self.address

class reference(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=100, null=True)
    file = models.FileField(upload_to='static/references')
    upload_date = models.DateTimeField(auto_now_add=True)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        f_dot, f_extension = extension.split('.')
        return f_extension

    # def size(self):
    #     # size = len(self.file)
    #     file_size = os.path.getsize(self.file)
    #     return file_size

    def __str__(self):
        return self.name
