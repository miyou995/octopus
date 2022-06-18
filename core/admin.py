from django.contrib import admin
from .models import Client, Contact, Category, Invoice, InvoiceItem, Solution, Service, Quote,  Offre, Fonctionalite, Status, Article
from django.contrib.auth.models import Group, User
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe

admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.unregister(Group)


class ContactAdmin(admin.ModelAdmin):     
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_per_page = 40
    list_filter = ('name', 'phone', 'email',)
    search_fields = ('id', 'phone', 'email')
    readonly_fields = ('date_sent',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    list_per_page = 40

# class SolutionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id','name')
#     list_per_page = 40

# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id','name')
#     list_per_page = 40

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor')
    list_display_links = ('id','autor')
    list_per_page = 40


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    list_per_page = 40



# class XYModelForm(forms.ModelForm)
#     class Meta:
#         fields = ('field1, field2', ...)
#         widgets = {
#             'field1': (any widget you like)
#         }

# @admin.register(XYModel)
# class XYModelAdmin(admin.ModelAdmin)
#     form = XYModelForm


def order_detail(obj):
    url = reverse('core:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">Detail</a>')

def order_pdf(obj):
    url = reverse('core:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')

order_pdf.short_description = 'Invoice'


class InvoiceItemInline(admin.TabularInline):
    model           = InvoiceItem
    raw_id_fields   = ['invoice']

@admin.display()
def total_da(obj):
    return ("%s" % obj.get_total_cost())


@admin.register(Invoice)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'client_phone' ,'client_email' ,'created' ,'updated' ,total_da,'paid', order_detail, order_pdf]
    list_display_links =('id', 'client')
    list_filter = ['paid','updated']
    list_editable = ['paid','client_phone' ,'client_email']
    inlines = [InvoiceItemInline] 
    # actions = [export_to_csv]
    list_per_page = 30





class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'fonctionalite', 'offre', 'quantity','included' )
    list_editable = ['quantity','included']
    list_filter = ( 'offre',)
    list_display_links = ('id','fonctionalite', 'offre',)
    list_per_page = 40

class StatusInline(admin.TabularInline):
    model   = Status
    fields   = ['fonctionalite','offre', 'included','quantity']
    extra = 0 

class OfferInline(admin.TabularInline):
    model           = Offre
    fields   = ['title', 'description',]
    extra = 0


class FuntionsInline(admin.TabularInline):
    model           = Fonctionalite
    fields   = ['title', 'description',]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_filter = ['name',]
    list_display_links = ['id', 'name', ]

    inlines = [OfferInline, FuntionsInline] 
    list_per_page = 30


class FonctionaliteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','service', ]
    list_filter = ['service']
    list_display_links = ['id', 'title']
    list_editable = ['service']

    inlines = [StatusInline] 
    list_per_page = 30



class OffreAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','service', 'price_month', 'price_year']
    list_filter = ['title','service', 'price_month', 'price_year']
    list_display_links = ['id', 'title', 'service' ,'price_month', 'price_year']

    inlines = [StatusInline] 
    list_per_page = 30


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id','title')
    list_per_page = 40

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Solution, SolutionAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Fonctionalite, FonctionaliteAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Offre, OffreAdmin)
admin.site.register(Article, ArticleAdmin)
