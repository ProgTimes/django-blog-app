from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 6, 'maxlength': 350, "class": "form-control", "placeholder": "Enter your comment"
    }), max_length=350, label="")
