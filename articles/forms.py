from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 80}))
    short_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'row': 20,}))

    class Meta:
        model = Article
        fields = ('title', 'short_description','thumbnail', 'tags', 'content',)