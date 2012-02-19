# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _

from filer.fields.image import FilerImageField


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey('categories.Category')
    pub_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __unicode__(self):
        return self.title


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(max_length=255)
    category = models.ForeignKey('categories.Category', null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now)
    image = FilerImageField()

    class Meta:
        verbose_name = _('Gallery Image')
        verbose_name_plural = _('Gallery Images')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pub_date = self.image.date_taken
        super(GalleryImage, self).save(*args, **kwargs)
