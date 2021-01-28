from django import forms
from .models import Post
from django.utils.translation import gettext_lazy as _

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'slug', 'thumbnail_img', 'post_snippet', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post title'}),
			'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Slug is automatically generated. It is OK to leave it empty'}),
			'thumbnail_img':forms.FileInput(),
			'post_snippet':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief extract, not more than 250 characters'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'slug', 'thumbnail_img', 'post_snippet', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post title'}),
			'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Slug is automatically generated. It is OK to leave it empty'}),
			'thumbnail_img':forms.FileInput(),
			'post_snippet':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief extract, not more than 250 characters'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}