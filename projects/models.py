from django.db import models

# Create your models here.

class project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='projects/images/')
    github_url=models.URLField(blank=True)
    live_url=models.URLField(blank=True)
    
    WEBDEV="WD";
    VIDEOEDIT="VE";
    DESIGN="DG";
    CATEGORY_CHOICES = [
        (WEBDEV, 'Web Development'),
        (VIDEOEDIT, 'Video Editing'),
        (DESIGN, 'Design'),
    ]
    category = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=WEBDEV)

    
    def __str__(self):
        return self.title