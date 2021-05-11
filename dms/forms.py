from django import forms
from .models import Seedling
from django.utils.translation import gettext_lazy as _

class AddSeedlingForm(forms.ModelForm):
	class Meta:
		model = Seedling
		fields = ('local_name', 'scientific_name', 'category', 'origin', 'nursery', 'description', 'remarks', 'quantity', 'seedling_img')

		widgets = {
			'local_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Local name'}),
			'scientific_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Scientific Name'}), 
			'category':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}),
			'origin':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Origin'}),
			'nursery':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nursery'}),
			'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
			'remarks':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Remarks'}),
			'quantity':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
			'seedling_img':forms.FileInput(),
		}

		labels = {
			'local_name':_(''),
			'scientific_name':_(''),
			'category':_(''),
			'origin':_(''),
			'nursery':_(''),
			'description':_(''),
			'remarks':_(''),
			'quantity':_(''),
			'seedling_img':_(''),
		}

class UpdateSeedlingForm(forms.ModelForm):
	class Meta:
		model = Seedling
		fields = ('local_name', 'scientific_name', 'category', 'origin', 'nursery', 'description', 'remarks', 'quantity', 'seedling_img')

		widgets = {
			'local_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Local name'}),
			'scientific_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Scientific Name'}), 
			'category':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}),
			'origin':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Origin'}),
			'nursery':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nursery'}),
			'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
			'remarks':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Remarks'}),
			'quantity':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
			'seedling_img':forms.FileInput(),
		}

		labels = {
			'local_name':_(''),
			'scientific_name':_(''),
			'category':_(''),
			'origin':_(''),
			'nursery':_(''),
			'description':_(''),
			'remarks':_(''),
			'quantity':_(''),
			'seedling_img':_(''),
		}