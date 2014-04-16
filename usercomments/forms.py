from django import forms
from .models import UserComment

class UserCommentForm(forms.Form):
    title = forms.CharField(max_length=500)
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = UserComment