from django import forms
from news.models import Newspaper, Topic, Redactor


class NewspaperCreationForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )
    published_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperUpdateForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Newspaper
        fields = ("title", "content", "topics",)


class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class TopicUpdateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class RedactorCreateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ("first_name",
                  "last_name",
                  "username",
                  "email",
                  )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = "__all__"
