
from django.db import models
from django.forms import DateField
from phone_field import PhoneField
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name

class Tags(models.Model):
    tag_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.tag_name

class IndustrySettings(models.Model):
    logo = models.ImageField(upload_to='images/logo/')
    phone = PhoneField()
    email = models.EmailField()
    office_time = models.CharField(max_length=16)
    mission = models.TextField()
    vision = models.TextField()
    goal = models.TextField()
    address = models.TextField(null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.email

class IndustryBranch(models.Model):
    branch_name = models.CharField(max_length=100, unique=True)
    branch_address = models.TextField()
    branch_phone = PhoneField()
    branch_email =models.EmailField()

    def __str__(self):
        return self.branch_name


class ContactHead(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.title


class BlogHead(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class BlogContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)
    image_blog = models.ImageField(upload_to='images/blog/')
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class TeamHead(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class TeamContent(models.Model):
    image_team = models.ImageField(upload_to='images/team/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    fb_account = models.CharField(max_length=100, null=True)
    twitter_account = models.CharField(max_length=100, null=True)
    linkedin_account = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class ProjectHead(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title     

class ProjectContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_project = models.ImageField(upload_to='images/project/')
    challange = models.TextField(null=True)
    solution = models.TextField(null=True)
    client = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    time_duration = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class WhyusHead(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title   


class WhyusContent(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class ServiceHead(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class ServiceContent(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    service_image = models.ImageField(upload_to='images/service/')

    def __str__(self):
        return self.title


class Aboutus(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    aboutus_image = models.ImageField(upload_to='images/aboutus/')

    def __str__(self):
        return self.title


class SlideShow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slide_image = models.ImageField(upload_to='images/slideshow/')
   

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    comment = models.TextField()
    testimonial_image = models.ImageField(upload_to='images/testmonial/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

