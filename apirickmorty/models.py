from django.db import models

class Characters(models.Model):  ##### Aqui eu realizei os models da minha aplicação que aparecem no ADMIN
    name = models.CharField(max_length= 80)
    status = models.CharField(max_length= 40)
    species = models.CharField(max_length= 60)
    type = models.CharField(max_length= 70)
    gender = models.CharField(max_length= 90)
    origin = models.URLField(max_length=255)
    location = models.CharField(max_length=255)
    episode = models.CharField(max_length=180)
    url = models.URLField(max_length=255)
    create = models.CharField(max_length=255)

    def __str__(self):
        return self.name

