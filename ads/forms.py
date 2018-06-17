from django.core.exceptions import ValidationError
from django.forms import ModelForm

from ads.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['blog']

    def clean_image(self):
        image = self.cleaned_data.get('URLimagen')
        if image is not None and 'URLimagen' not in image.content_type:
            raise ValidationError('El archivo seleccionado no es valido')
        return image

    def clean(self):
        super().clean() # llamada al metodo clean de la superclase

