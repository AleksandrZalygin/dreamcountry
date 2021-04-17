from django.db import models    


CLIMATE_CHOICES = (
    ('Лето', 'Лето'),
    ('Зима', 'Зима'),
)
WORLD_CHOICES = (
    ('Европа', 'Европа'),
    ('Азия', 'Азия'),
    ('Америка', 'Америка'),
    ('Австралия и Океания', 'Австралия и Океания'),
)
WORK_CHOICES = (
    ('Да', 'Да'),
    ('Нет', 'Нет'),
)
class Country(models.Model):
    title = models.CharField(max_length=60,)
    climate = models.CharField(max_length=60, choices=CLIMATE_CHOICES, default='Лето')
    world = models.CharField(max_length=60, choices=WORLD_CHOICES, default='Европа')
    work = models.CharField(max_length=60, choices=WORK_CHOICES, default='Нет')
    medicine = models.CharField(max_length=60, choices=WORK_CHOICES, default='Да')
    citizenship = models.CharField(max_length=60, choices=WORK_CHOICES, default='Да')


    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'