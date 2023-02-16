from django.db import models

# Create your models here.
class exp(models.Model):
    title=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='homepage/images/explogos/')
    url=models.URLField(blank=True)
    fromdate=models.DateField()
    present=models.BooleanField(default=False)
    todate=models.DateField()

    def __str__(self):  
        return self.title
