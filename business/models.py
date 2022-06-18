from django.db import models
from tinymce import models as tinymce_models
from markdownx.models import MarkdownxField

from django.core.exceptions import ValidationError
# Create your models here.
class Business(models.Model):
    name         = models.CharField(verbose_name="Nom de l'entreprise", max_length=100)
    logo         = models.ImageField(upload_to='images/logos', verbose_name='Logo')
    logo_negatif = models.ImageField(upload_to='images/slides', verbose_name="Logo négatif")
    title        = models.CharField(verbose_name="Titre", max_length=50, blank=True)
    adress       = models.CharField(verbose_name="Adresse", max_length=50, blank=True)
    email        = models.EmailField(verbose_name="email de l'entreprise", max_length=50, blank=True)
    phone        = models.CharField(verbose_name="numéro de téléphone de l'entreprise", max_length=50, blank=True)
    about        = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)
    facebook     = models.URLField(verbose_name="Lien page Facebook", max_length=300, blank=True, null=True)
    insta        = models.URLField(verbose_name="Lien page Instagram", max_length=300, blank=True, null=True)
    linkedin     = models.URLField(verbose_name="Lien page LinkedIn", max_length=300, blank=True, null=True)
    messenger    = MarkdownxField(verbose_name='Facebook Messenger', blank=True, null=True)
    tag_header    = MarkdownxField(verbose_name='Google tag manager header', blank=True, null=True)
    tag_body    = MarkdownxField(verbose_name='Google tag manager body', blank=True, null=True)
    pixel        = MarkdownxField(verbose_name='Facebook Pixel', blank=True, null=True)
    analytics    = MarkdownxField(verbose_name='Google Analytics', blank=True, null=True)
    analytics2   = MarkdownxField(verbose_name='Analytics 2', blank=True, null=True)
    messenger_script = MarkdownxField()

    # actif  = models.BooleanField(verbose_name='Active', default=False)
    # is_big  = models.BooleanField(verbose_name='Grande photo (1920 x 570)', default=False)
    # is_small  = models.BooleanField(verbose_name='Medium photo (720 x 540)', default=False)

    class Meta:
        verbose_name = '1. Infomation'
        verbose_name = '1. Infomations'

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter d'entreprise")

class Slide(models.Model):
    photo  = models.ImageField(verbose_name="Photo 1", upload_to=None, height_field=None, width_field=None, max_length=None)
    url = models.URLField(verbose_name="lien", max_length=200)
    class Meta:
        verbose_name = '2. Grande Photo'
        verbose_name = '2. Grande Photo'

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter d'autres slides")

class Banner(models.Model):
    photo      = models.ImageField(verbose_name="Photo 2", upload_to=None, height_field=None, width_field=None, max_length=None)
    title      = models.CharField(verbose_name="Grand titre de la photo", max_length=50, blank=True, null=True) 
    sub_title  = models.CharField(verbose_name="Sous titre de la photo", max_length=50, blank=True, null=True) 
    url        = models.URLField(verbose_name="Lien", max_length=250)

    class Meta:
        verbose_name = '3. Banner'
        verbose_name = '3. Banner'
    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter d'autres Banners")