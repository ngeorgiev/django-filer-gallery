from django import forms

from filer.models import Image


class UploadImageFileForm(forms.ModelForm):

    class Meta:
        model = Image
