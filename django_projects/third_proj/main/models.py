from django.db import models

# Create your models here.
class Notebooks(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    article = models.IntegerField()
    img = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'    

    def __str__(self) -> str:
        return f'{self.title}'

