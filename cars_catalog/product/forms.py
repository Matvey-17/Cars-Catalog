from django import forms
from product.models import Car


class CommentForm(forms.Form):
    content = forms.CharField(label='Комментарий', max_length=1024)


class AddCarForm(forms.Form):
    make = forms.CharField(label='Марка', max_length=256)
    model = forms.CharField(max_length=256, label='Модель')
    year = forms.CharField(max_length=10, label='Год выпуска')
    description = forms.CharField(max_length=1024, label='Описание')


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']
