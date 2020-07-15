from django import forms
from tweets.models import TweetModel

class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetModel
        fields = ['content']

    def cleaned_data():
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise form.ValidationError('This is not valid')
        return content