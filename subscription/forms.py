from django import forms
from .models import Subs
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
	class Meta:
		model = Subs
		fields = ('subscriber_first_name', 'subscriber_last_name', 'subscriber_email')

		labels = {
			'subscriber_first_name': _(''),
			'subscriber_last_name': _(''),
			'subscriber_email': _('')
		}

		widgets = {
			'subscriber_first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name', 'label':''}),
			'subscriber_last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}),
			'subscriber_email':forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'Email'})
		}