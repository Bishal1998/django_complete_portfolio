from django.db import models

# Create your models here.
class Hero(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    car_1 = models.CharField(max_length=50)
    car_2 = models.CharField(max_length=50)
    car_3 = models.CharField(blank=True ,max_length=50)
    car_4 = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.first_name

class About(models.Model):
    profile = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    txt_1 = models.TextField()
    txt_2 = models.TextField()
    txt_3 = models.TextField(blank=True)
    html = models.CharField(max_length=5)
    css = models.CharField(max_length=5)
    python = models.CharField(max_length=5)
    graphic = models.CharField(max_length=5)

    def __str__(self):
        return self.email
    
class Services(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    detail = models.TextField()

    def __str__(self):
        return self.title
    

class Stats(models.Model):
    work = models.CharField(max_length=50)
    exp = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    award = models.CharField(max_length=50)

    def __str__(self):
        return self.work
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to = "static/img")
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Services, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.title
    
class Testimony(models.Model):
    image = models.ImageField(upload_to = 'static/img')
    name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    