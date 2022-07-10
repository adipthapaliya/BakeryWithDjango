from django import forms
from userAccount.models import UserMessageModel

class UserMessageForm(forms.ModelForm):
    class Meta:
        model=UserMessageModel
        fields ="__all__"