from django import forms
from polls.models import Question


class QuestionForm(forms.ModelForm):

  class Meta:
    model = Question
    fields = ('question_text', 'limit_date', 'pub_date')
