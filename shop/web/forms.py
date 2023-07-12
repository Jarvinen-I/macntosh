from django import forms
from django.forms import ModelForm, Textarea

from .models import Customer

from django.core.exceptions import ValidationError


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'type': 'text',
                                                 'class': 'form-control input-text',
                                                 'id': 'name',
                                                 'placeholder': 'Имя',
                                                 'data-rule': 'minlen:4',
                                                 'data-msg': 'Введите не менее 4 символов',
                                                 })
        self.fields['email'].widget.attrs.update({'type': 'email',
                                                  'class': 'form-control input-text',
                                                  'id': 'email',
                                                  'placeholder': 'Email',
                                                  'data-rule': 'email',
                                                  'data-msg': 'Введите действительный адрес электронной почты'
                                                  })
        self.fields['phone'].widget.attrs.update({'type': 'text',
                                                  'class': 'form-control input-text',
                                                  'id': 'subject',
                                                  'placeholder': 'Телефон',
                                                  'data-rule': 'minlen:11',
                                                  'data-msg': 'Введите действительный номер телефона в формате '
                                                              '89001112233'
                                                  })
        self.fields['message'].widget.attrs.update({'type': 'text-area',
                                                    'class': 'form-control input-text text-area',
                                                    'id': 'message',
                                                    'placeholder': 'Сообщение',
                                                    'data-rule': 'required',
                                                    'data-msg': 'Напишите сообщение',
                                                    })


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
