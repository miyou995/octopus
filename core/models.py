from telnetlib import RCP
from django.db import models
# Create your models here.
from tinymce import models as tinymce_models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)

class Category(models.Model):
    name  = models.CharField(verbose_name=_('Nom du DAS'), max_length=100)
    title  = models.CharField(verbose_name=_('Petit text'), max_length=100, blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    icon  = models.FileField(upload_to='images/categories', null=True, blank=True)
    
    class Meta:
        verbose_name ="Catégorie"
    
    def __str__(self):
        return self.name

class Solution(models.Model):
    name        = models.CharField(verbose_name=_('sous catégorie'), max_length=100)
    title       = models.TextField(verbose_name=_('Petit text'),blank=True, null=True)
    description = tinymce_models.HTMLField(verbose_name='Déscription du produit', blank=True, null=True)
    icon        = models.ImageField(upload_to='images/categories', null=True, blank=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name  = models.CharField(verbose_name=_('Nom du Service'), max_length=100)
    slug = models.SlugField()
    title  = models.CharField(verbose_name=_('Petit text'), max_length=300)
    photo  = models.ImageField(upload_to="images/services",verbose_name=_('img 2'),blank=True, null=True)
    image = models.FileField( upload_to="images/services/", blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("DAS categorie"), on_delete=models.CASCADE)
    description = tinymce_models.HTMLField(verbose_name='Déscription du produit', blank=True, null=True)
    icon  = models.CharField(verbose_name=_('nom de l icon du site https://fontawesome.com/icons'), max_length=100)
    priority  = models.IntegerField(verbose_name=_('ordre / priorité'))
    to_home_page = models.BooleanField(verbose_name="ajouter a la page d'accueil", default=False)
    to_footer = models.BooleanField(verbose_name="ajouter au footer", default=False)
    # actif  = models.BooleanField(default=True)
    # created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    # updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("core:service-detail", kwargs={"slug": self.slug})
    
# class Article(models.Model):
#     pass                    

class Contact(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank =True)
    subject     = models.CharField(verbose_name=_("Sujet"), max_length=50, blank=True,null=True)
    message     = models.TextField(verbose_name=_("Message"), blank=True, null=True)
    date_sent   = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)
        verbose_name = 'Formulaire de contact'
        verbose_name_plural = 'Formulaire de contact'

class Quote(models.Model):
    name = models.TextField(verbose_name=_("la citation"))
    actif = models.BooleanField(default=True)
    autor = models.CharField(verbose_name=_("auteur"), max_length=100)
    function = models.CharField(verbose_name=_("Fonction"), max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.autor)

class Client(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField( upload_to="images/clients")

    def __str__(self):
        return self.name

class Article(models.Model):
    title         = models.CharField( max_length=150, verbose_name='Titre')
    slug          = models.SlugField()
    aperçu        = models.CharField( max_length=300, verbose_name='aperçu', blank=True, null=True)
    chapo         = models.CharField( max_length=300, verbose_name='chapô ',blank=True, null=True)
    quote         = models.CharField( max_length=300, verbose_name='phrase mise en avant ', blank=True, null=True)
    texte_haut    = tinymce_models.HTMLField(verbose_name='texte haut', blank=True, null=True)
    texte_bas     = tinymce_models.HTMLField(verbose_name='texte bas', blank=True, null=True)
    card_img     = models.ImageField(upload_to="images/")
    banner        = models.ImageField(upload_to="images/")
    publish       = models.BooleanField(default=True)
    actif         = models.BooleanField(default=True)
    created       = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated       = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    def __str__(self):
        return str(self.title)
    def get_absolute_url(self):
        return reverse("core:article_detail", kwargs={"slug": self.slug})

class Invoice(models.Model):
    client          = models.CharField(max_length=300,verbose_name='Client')
    client_rc       = models.CharField(max_length=300,verbose_name='RC Client')
    client_nif      = models.CharField(max_length=300,verbose_name='Nif Client')
    client_art      = models.CharField(max_length=300,verbose_name="Numéro d'article du client")
    client_adresse  = models.CharField(max_length=300,verbose_name='Adresse Client')
    client_phone    = models.CharField(max_length=300,verbose_name='Téléphone Client')
    client_email    = models.EmailField(max_length=300,verbose_name='Email Client')
    invoice_number  = models.IntegerField(verbose_name='Numéro de facture')
    invioce_date    = models.DateField(verbose_name=_("Date "), blank = True, null = True) 
    created       = models.DateTimeField(auto_now_add=True, verbose_name=_("Crée"))
    updated       = models.DateTimeField(auto_now=True, verbose_name=_("Modifié"))
    note          = models.TextField(blank=True, null=True, verbose_name=_("Note"))
    paid          = models.BooleanField(default=False, verbose_name=_("Payé"))
    discount      = models.DecimalField( max_digits=10, decimal_places=2, default=0, verbose_name="Réduction")

    def __str__(self):
        return f'facture N°:  {self.invoice_number} doit {self.client}'

    def save(self, *args, **kwargs):
        try:
            last_num = Invoice.objects.last().invoice_number
            self.invoice_number = last_num =+ 1
        except:
            self.invoice_number = 1
        super().save(*args, **kwargs) 
        return sum(item.get_cost() for item in self.items.all())


    def get_total_cost(self):
        items_cost = sum(item.get_cost() for item in self.items.all())
        total_cost = items_cost - self.discount
        # if total_cost < 0:
        #     total_cost = 0

        return total_cost




class InvoiceItem(models.Model):
    invoice    = models.ForeignKey(Invoice,related_name='items', verbose_name=(_("Facture")), on_delete=models.CASCADE)
    description = models.CharField(max_length=300,verbose_name='Description')
    price    = models.DecimalField( max_digits=10, decimal_places=2, verbose_name=_("Prix"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantité"))

    def __str__(self):
        return str(self.description)
    def get_cost(self):
        return self.price * self.quantity



class Offre(models.Model):
    title        = models.CharField(verbose_name=_('Offre'), max_length=100)
    description  = models.TextField( blank=True, null=True)
    service              = models.ForeignKey(Service, on_delete=models.CASCADE,blank=True, null=True)
    priority     = models.IntegerField(verbose_name=_('ordre / priorité'), blank=True, null=True)
    price_month         = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    price_year        = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('id',)
        verbose_name = 'offre'
        verbose_name_plural = 'offres'   


class Fonctionalite(models.Model):
    title        = models.CharField( max_length=100)
    service      = models.ForeignKey(Service, on_delete=models.CASCADE,blank=True, null=True)
    description  = models.TextField( blank=True, null=True)
    priority  = models.IntegerField(verbose_name=_('ordre / priorité'), blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('id',)
        verbose_name = 'fonctionalite'
        verbose_name_plural = 'fonctionalites' 

class Status(models.Model):
    offre                = models.ForeignKey(Offre, verbose_name=_("offre"), on_delete=models.CASCADE,blank=True, null=True)
    fonctionalite        = models.ForeignKey(Fonctionalite,related_name="status", verbose_name=_("fonctionalite"), on_delete=models.CASCADE,blank=True, null=True)
    included             = models.BooleanField(verbose_name="inclu dans l'offre", default=False)
    quantity             = models.CharField(verbose_name=_('quantité'), max_length=100,blank=True, null=True)
    created              = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated              = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)

    def __str__(self):
        return str(self.fonctionalite)

    class Meta:
        ordering = ('id',)
        verbose_name = 'status'
        verbose_name_plural = 'statuss' 