from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name',
                  'author_surname',
                  'author_email',
                  'content']