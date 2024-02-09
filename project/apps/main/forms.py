from django import forms
from .models import FreeCall


class Select(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        if index == 0:
            label = 'Выберите услугу'
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['class'] = 'styled'
        return option

class Form(forms.ModelForm):
    class Meta:
        model = FreeCall
        fields = ('full_name', 'e_mail', 'subject', 'message', 'phone_number', 'town')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Ведите ваше имя', 'class': 'form-input'}),
            'town': forms.TextInput(attrs={'placeholder': 'Ведите ваш Айыл', 'class': 'form-input'}),
            'e_mail': forms.EmailInput(attrs={'placeholder': 'Ваш Email', 'class': 'form-input', 'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,10}$'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Ваш номер телефона', 'class': 'form-input', 'type': 'tel', 'pattern': '^[0-9]{11,15}$'}),
            'message': forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'id': 'message'}),
            'subject': Select(attrs={'id': 'choose-serv'}),
        }


class ResultForm(forms.Form):
    oder_number = forms.IntegerField(label=False, widget=forms.TextInput(attrs={'class':'search_input', 'placeholder':'Номер', "required": "required"}))
    pin = forms.IntegerField(label=False, widget=forms.TextInput(attrs={'class':'search_input', 'placeholder':'Кодовое слово (Пин)', "required": "required"}))

