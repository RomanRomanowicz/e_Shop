from django import forms
from store.models.products import Image


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'image')