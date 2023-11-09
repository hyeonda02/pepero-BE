from django.db import models

CHOCO = (
    ('초코','초코'),
    ('딸기','딸기'),
    ('화이트','화이트'),
    ('녹차','녹차'),
    ('블루베리','블루베리'),
)
SAUCE = (
    ('초코','초코'),
    ('딸기','딸기'),
    ('화이트','화이트'),
    ('녹차','녹차'),
    ('블루베리','블루베리'),
)
DECO = (
    ('하트','하트'),
    ('별','별'),
    ('아몬드','아몬드'),
    ('오레오','오레오'),
    ('스프링','스프링'),
)

# Create your models here.
class Pepero(models.Model):
    choco = models.TextField(verbose_name='초코',null=True, blank=True)
    sauce = models.TextField(verbose_name='소스',null=True, blank=True)
    deco = models.TextField(verbose_name='데코',null=True, blank=True)
    content = models.TextField(verbose_name='편지',null=True, blank=True) 
    