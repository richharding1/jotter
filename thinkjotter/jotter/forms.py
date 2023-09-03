from django import forms
from .models import Entry, Category, Hashtag

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['date', 'notes', 'literature']
        labels = {'date': 'Date', 'notes': 'Notes', 'literature': 'References'}
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}), 'notes': forms.Textarea(attrs={'cols': 80})}

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        labels = {'category': 'Category'}

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['tag']
        labels = {'tag': 'Hashtag'}

