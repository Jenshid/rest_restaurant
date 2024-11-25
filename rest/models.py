# Create your models here.
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Registration(models.Model):
    Password = models.CharField(max_length=128, null=True)
    User_role = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Add other fields as needed
    
    def __str__(self):
        return self.user.username
    

class HomepageContent(models.Model):
    main_title = models.CharField(max_length=200, default='Welcome to the Homepage', null=True)
    sub_title = models.TextField(default='This is the subtitle of the homepage')
    image = models.ImageField(upload_to='homepage_images/', blank=True, null=True)

    def __str__(self):
        return self.main_title   
  

class AboutUs(models.Model):
    content = models.TextField(max_length = 800, null = True)
    def __str__(self):
        return self.content
    

class Ourpeople(models.Model):
    content = models.TextField(max_length = 800, null = True)
    def __str__(self):
        return self.content


class Mission_vision(models.Model):
    content = models.TextField(max_length = 800, null = True)
    def __str__(self):
        return self.content



class chairman(models.Model):
    content = models.TextField(max_length = 800, null = True)
    def __str__(self):
        return self.content
    


class Manage_Restaurant(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='restaurants/images/',blank=True, null=True)
    logo = models.ImageField(upload_to='restaurants/logos/',blank=True, null=True)
    description = models.TextField(max_length = 800, null = True)
    # Location information
    LOCATION_CHOICES = [
        ('local', 'Local'),
        ('international', 'International'),
    ]
    location_type = models.CharField(max_length=20, choices=LOCATION_CHOICES, null= True)
    
    home_page_order = models.IntegerField(default=99, null = True )
    brand_page_order = models.IntegerField(default=99, null = True)
    
    reservation_url = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    

    def _str_(self):
        return self.name

    class Meta:
        ordering = ['home_page_order', 'brand_page_order']


class Images_rest(models.Model):
    restaurant_img= models.ForeignKey(Manage_Restaurant,on_delete=models.CASCADE,related_name='images')
    img = models.ImageField(upload_to='homepage_images/', blank=True, null=True)
    
    def __str__(self):
        return str(self.img)
    
class Media_media(models.Model):
    content = HTMLField(max_length = 800, null = True)
    title = models.TextField(max_length = 50, null = True)
    def __str__(self):
        return self.content 
    

class Subscription(models.Model):
    email  = models.TextField(max_length = 50, null = True)
    def __str__(self):
        return self.content 
    
class contact_US(models.Model):
    title = models.CharField(max_length = 50, null = True)
    place = models.CharField(max_length =255, null = True)
    phone = models.CharField(max_length = 20, null = True)
    description = models.TextField(max_length = 800, null = True)
    email = models.EmailField(max_length = 255, null = True)
    pinterest_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(max_length = 255, null = True)
    def __str__(self):
        return self.content
    
class Careers_us(models.Model):
    brand = models.CharField(max_length = 50, null = True)
    department = models.CharField(max_length =55, null = True)
    job_title = models.CharField(max_length = 25, null = True)
    job_description = models.TextField(max_length = 300, null = True)
    contact_email = models.EmailField(max_length = 55, null = True)
    job_code =  models.CharField(max_length = 20, null = True)
    job_responsibilities = models.TextField(max_length = 800, null = True)
    job_requirement = models.TextField(max_length = 800, null = True)
    salary_range = models.CharField(max_length = 20, null = True)
    age_limit = models.CharField(max_length = 20, null = True)
    place = models.CharField(max_length = 20, null = True)
     # Define employment type with the intended spelling and choices
    EMPLOYMENT_TYPE_CHOICES = [
        ('Permanent', 'Permanent'),
        ('Contract', 'Contract'),
        ('none', 'None'),
    ]

    employment_type = models.CharField(max_length=35, choices=EMPLOYMENT_TYPE_CHOICES, null=True)
    def __str__(self):
        return self.brand
   

class JobApplication(models.Model):
    full_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=25, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(max_length=70, null=True)
    position = models.CharField(max_length=20, null=True)
    cv = models.FileField(null=True)
    career = models.ForeignKey(Careers_us, on_delete=models.CASCADE, null=True, related_name='applications')

    def __str__(self):
        return self.full_name if self.full_name else f"Application {self.id}"  # Fallback if full_name is None
