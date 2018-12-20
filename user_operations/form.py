from django import forms
from user_operations.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("content",)


class CommentValiForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("user", "content", "product")