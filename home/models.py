from django.db import models



class Pyladies(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    number = models.IntegerField()
    event = models.CharField(max_length=50)
    about_self = models.TextField()

    class Meta:
        verbose_name_plural = "Pyladies"

    def __str__(self):
        return self.name

class DevcHackatron (models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    number = models.IntegerField()
    event = models.CharField(max_length=50)
    about_self = models.TextField()

    class Meta:
        verbose_name_plural = "DevC Hackatron "

    def __str__(self):
        return self.name

class DscFuto (models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    number = models.IntegerField()
    event = models.CharField(max_length=50)
    about_self = models.TextField()

    class Meta:
        verbose_name_plural = "Dsc Futo"

    def __str__(self):
        return self.name