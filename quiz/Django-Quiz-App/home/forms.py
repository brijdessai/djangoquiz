from django.forms import ModelForm
from django import forms
import time
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
    def __init__(self, *args, **kwargs):
        super(createuserform, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'onchange':'enableBeforeUnload()'})
        self.fields['password'].widget.attrs.update({'onchange':'enableBeforeUnload()'})
        
class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"