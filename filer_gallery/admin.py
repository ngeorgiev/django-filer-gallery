# -*- coding: utf-8 -*-
from django.contrib import admin

from filer_gallery.models import Gallery, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    exclude = ('pub_date',)
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title')
    list_editable = ('title',)
    exclude = ('pub_date',)
    prepopulated_fields = {'slug': ('title',) }
    inlines = [GalleryImageInline]


admin.site.register(Gallery, GalleryAdmin)
