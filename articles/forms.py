from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'