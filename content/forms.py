from dataclasses import field
from django.forms import ModelForm, widgets
from .models import *

class   ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['baslık','yazi','resim','imdb','isim','tarih']
    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)
        
        self.fields['resim'].widget.attrs.update({'class':'movie-picture'})
        self.fields['imdb'].widget.attrs.update({'class':'movie-imdb'})
        
