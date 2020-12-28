from django import forms

from app.models import AppPost

class CreateAppPostForm(forms.ModelForm):
	class Meta:
		model = AppPost
		fields = ['title', 'body', 'image']

class UpdateAppPostForm(forms.ModelForm):
	
	class Meta:
		model = AppPost
		fields = ['title', 'body', 'image']

	def save(self,commit=True):
		app_post = self.instance
		app_post.title = self.cleaned_data['title']
		app_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			app_post.image = self.cleaned_data['image']

		if commit:
			app_post.save()
		return app_post	