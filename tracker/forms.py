from django import forms
from tracker.models import Log

# class UpdateForm(forms.Form):
#     notes = forms.CharField(label='notes', max_length=500, required=False)
#     date = forms.DateField(label='date', widget=forms.DateTimeInput(), required=True)
#     area = forms.ChoiceField(required=True)


class LogForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = ['area', 'date', 'notes' ]
        success_url = "/tracker/log"

    def __init__(self, *args, **kwargs):
        return super(LogForm, self).__init__(*args, **kwargs)


# class NewLog(forms.Form):
