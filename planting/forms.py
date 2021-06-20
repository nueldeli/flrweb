from django import forms
from .models import PlantingProgram, Item
from django.utils.translation import gettext_lazy as _

class AddPlantingProgram(forms.ModelForm):
	class Meta:
		model = PlantingProgram
		fields = ('program_date', 'program_name', 'program_location', 'program_area', 'program_species', 'program_participant', 'program_img')

		widgets = {
			'program_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Program date'}),
			'program_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Program name'}),
			'program_location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Program location'}),
			'program_area':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Area covered'}),
			'program_species':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Species'}),
			'program_participant':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Participant'}),
			'program_img':forms.FileInput(),

		}

		labels = {
			'program_date':_(''),
			'program_name':_(''),
			'program_location':_(''),
			'program_area':_(''),
			'program_species':_(''),
			'program_participant':_(''),
			'program_img':_(''),
		}

class UpdatePlantingProgram(forms.ModelForm):
	class Meta:
		model = PlantingProgram
		fields = ('program_date', 'program_name', 'program_location', 'program_area', 'program_species', 'program_participant', 'program_img')

		widgets = {
			'program_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Program date'}),
			'program_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Program name'}),
			'program_location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Program location'}),
			'program_area':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Area covered'}),
			'program_species':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Species'}),
			'program_participant':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Participant'}),
			'program_img':forms.FileInput(),

		}

		labels = {
			'program_date':_(''),
			'program_name':_(''),
			'program_location':_(''),
			'program_area':_(''),
			'program_species':_(''),
			'program_participant':_(''),
			'program_img':_(''),
		}

class AddItem(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('item_local_name', 'item_scientific_name', 'item_img')

		widgets = {
			'item_local_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Local name'}),
			'item_scientific_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Scientific name'}),
			'item_img':forms.FileInput()
		}

		labels = {
			'item_local_name':_(''),
			'item_scientific_name':_(''),
			'item_img':_('')
		}

class UpdateItem(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('item_local_name', 'item_scientific_name', 'item_img')

		widgets = {
			'item_local_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Local name'}),
			'item_scientific_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Scientific name'}),
			'item_img':forms.FileInput()
		}

		labels = {
			'item_local_name':_(''),
			'item_scientific_name':_(''),
			'item_img':_('')
		}