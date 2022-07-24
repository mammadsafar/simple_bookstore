from django import forms

# from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Book, Comment
from ckeditor.fields import CKEditorWidget, RichTextField


class CostumeBookUpdate(forms.ModelForm):
    """Form for comments to the article."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    class Meta:
        model = Book
        fields = ("title", "description", "price", "cover", "status", "author")
        widgets = {
            # "description": forms.CharField(widget=RichTextField()),
            "description": CKEditorWidget(config_name='default'),
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "cover": forms.FileInput(attrs={'class': 'form-control'}),
            "status": forms.Select(attrs={'class': 'form-select'}),
            "author": forms.TextInput(attrs={'class': 'form-control'}),
        }
    #
    # title = forms.CharField(attrs={'class': 'form-control'})
    # price = forms.DecimalField(attrs={'class': 'form-select'})
    # cover = forms.ImageField(attrs={'class': 'form-select'})
    # status = forms.Select(attrs={'class': 'form-select'})


class CommentForm(forms.ModelForm):
    """Form for comments to the article."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = Comment
        fields = ("text", 'recommended')
        widgets = {
            "text": forms.TextInput(attrs={'class': 'form-control'}),
            "recommended": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
