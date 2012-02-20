# -*- coding: utf-8 -*-
from django.utils import simplejson
from filer_gallery import settings as filer_gallery_settings

from django.views.generic.dates import (ArchiveIndexView, YearArchiveView,
        MonthArchiveView, DayArchiveView)



class ConfigMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ConfigMixin, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context


class GalleryArchiveIndexView(ArchiveIndexView, ConfigMixin):
    def get_context_data(self, **kwargs):
        context = super(GalleryArchiveIndexView, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['SKITTER_CONFIG'] = simplejson.dumps(filer_gallery_settings.SKITTER_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context


class GalleryYearArchiveView(YearArchiveView, ConfigMixin):

    make_object_list = True

    def get_context_data(self, **kwargs):
        context = super(GalleryYearArchiveView, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['SKITTER_CONFIG'] = simplejson.dumps(filer_gallery_settings.SKITTER_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context


class GalleryMonthArchiveView(MonthArchiveView, ConfigMixin):
    def get_context_data(self, **kwargs):
        context = super(GalleryMonthArchiveView, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['SKITTER_CONFIG'] = simplejson.dumps(filer_gallery_settings.SKITTER_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context


class GalleryDayArchiveView(DayArchiveView, ConfigMixin):
    def get_context_data(self, **kwargs):
        context = super(GalleryDayArchiveView, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['SKITTER_CONFIG'] = simplejson.dumps(filer_gallery_settings.SKITTER_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context
