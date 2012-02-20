# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.db.models import Max
from django.utils.translation import ugettext as _

from filer.fields.image import FilerImageField


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    pub_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __unicode__(self):
        return self.title


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name="images")
    pub_date = models.DateTimeField(default=datetime.now)
    image = FilerImageField()
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']
        verbose_name = _('Gallery Image')
        verbose_name_plural = _('Gallery Images')

    def __unicode__(self):
        """Return the FilerImage name"""
        return u"%s" % self.image

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pub_date = self.image.date_taken
        if not self.order:
            last = self.gallery.images.aggregate(Max('order'))['order__max'] or 0
            self.order = last + 1
        super(GalleryImage, self).save(*args, **kwargs)
