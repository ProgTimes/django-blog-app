from django import forms

from blog.models import Post


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 6, 'maxlength': 350, "class": "form-control", "placeholder": "Enter your comment"
    }), max_length=350, label="")


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Content'}))

    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'category']
