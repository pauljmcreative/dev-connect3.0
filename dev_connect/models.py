from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class StudentProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    tag_line = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    linkedin_link = models.CharField(max_length=50, blank=True)
    github_link = models.CharField(max_length=50, blank=True)
    website_link = models.CharField(max_length=50, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    skills = models.TextField(blank=True)
    favorite_snack = models.CharField(max_length=50, blank=True)
    dream_job = models.TextField(blank=True)
    favorite_tech = models.CharField(max_length=50, blank=True)
    hidden_talent = models.CharField(max_length=50, blank=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user_id.username} Profile'

    # def save(self, *args, **kwargs):
    #     super(StudentProfile, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class Project(models.Model):
    title = models.CharField(max_length=50)
    hosted_link = models.CharField(max_length=50)
    github_link = models.CharField(max_length=50)
    screenshot = models.ImageField(upload_to='projects', blank=True)
    description = models.TextField()
    tech = models.TextField()
    teammates = models.TextField()
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     super(StudentProfile, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
