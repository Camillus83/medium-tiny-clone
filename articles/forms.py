from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Article, Note
from django import forms

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Article Body')
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 80, 'placeholder':'Article Title'}), label='Article Title', max_length=60)
    short_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'row': 20, 'placeholder': 'Short Description'}), label='Short Description', max_length=160)
    thumbnail = forms.FileField(widget=forms.FileInput(), label='Article Cover')

    class Meta:
        model = Article
        fields = ('title', 'short_description','thumbnail', 'tags', 'content',)
    
    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        title = cleaned_data.get('name')
        short_description = cleaned_data.get('short_description')
        content = cleaned_data.get('content')

        if not title and not short_description and not content:
            raise forms.ValidationError('Empty fields')


class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 80}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'row': 20,}))

    class Meta:
        model = Note
        fields = ('title', 'content',)

   
