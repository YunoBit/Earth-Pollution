from django import forms 

from apps.news.models import News


class NewsCreateForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title','description','image']


class NewsUpdateForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title','description','image']