# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from django.core.exceptions import ValidationError
from .models import Clue
from django.utils.encoding import smart_unicode

class ClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ["title","clue_type","short","content"]
        widgets = {
          'short': forms.Textarea(attrs={'rows':2, 'cols':10}),
        }