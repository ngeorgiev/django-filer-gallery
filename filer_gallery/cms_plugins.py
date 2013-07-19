from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from filer_gallery.models import FilerGalleryPluginModel


class FilerGalleryPlugin(CMSPluginBase):
    name = _('Gallery Plugin')
    model = FilerGalleryPluginModel
    render_template = 'filer_gallery/gallery_plugin.html'

    def render(self, context, instance, placeholder):
        context = super(FilerGalleryPlugin, self).render(context, instance, placeholder)
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(FilerGalleryPlugin)
