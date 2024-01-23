from django.db import models

# Create your models here.


from django.db import models

class Company_data(models.Model):
    company_name = models.CharField(max_length=255)
    company_location =  models.CharField(max_length=255) 

    def __str__(self):
        return self.company_name

