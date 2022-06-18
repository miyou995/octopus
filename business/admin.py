from django.contrib import admin
from .models import Business, Banner, Slide
from django.utils.html import format_html

# Register your models here.
class BusinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    
    # def has_add_permission(self, request):
    #     return False


class BannerAdmin(admin.ModelAdmin):
    def image_tag(self):
        return format_html('<img src="{}" height="150"  />'.format(self.photo.url))
        
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ('id', 'photo', 'title', 'sub_title', 'url')
    list_display_links = ('id', 'photo')
    list_editable = ['title', 'sub_title', 'url']
    
    # def has_add_permission(self, request):
    #     return False

# class SlideAdmin(admin.ModelAdmin):
#     def image_tag(self):
#         return format_html('<img src="{}" height="150"  />'.format(self.photo.url))
#     image_tag.short_description = 'Image'
#     image_tag.allow_tags = True
#     list_display = ('id', image_tag, 'url')
#     list_display_links = ('id', image_tag)
#     list_editable = ['url']
    
    # def has_add_permission(self, request):
    #     return False


admin.site.register(Business, BusinesAdmin)
admin.site.register(Banner, BannerAdmin)
# admin.site.register(Slide, SlideAdmin)
