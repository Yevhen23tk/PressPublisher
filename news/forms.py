from django.forms import forms
from django.forms import ModelForm

from news.models import Newspaper

# class NewspaperCreationForm(forms.ModelForm):
#     class Meta:
#         model = Newspaper
#         fields = "__all__"
#
#
# class NewspaperUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Newspaper
#         fields = ("title", "content", "topics",)


from django import forms
from django.forms import ModelForm

from news.models import Newspaper


class NewspaperCreationForm(ModelForm):
    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperUpdateForm(ModelForm):
    class Meta:
        model = Newspaper
        fields = ("title", "content", "topics")
