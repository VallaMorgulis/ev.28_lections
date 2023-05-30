from django.db import models

# Create your models here.
class Phones(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    img = models.ImageField(upload_to='images')
    description = models.TextField(blank=True)
    color = models.CharField(max_length=40)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'    

    def __str__(self) -> str:
        return f'{self.title}'