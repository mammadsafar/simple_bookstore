from django import forms

# from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Plan, Subscription, OrderDetail


class OrderDetailForm(forms.ModelForm):
    """Form for comments to the article."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    class Meta:
        model = OrderDetail
        fields = ("user", "plan", "payment_status")
