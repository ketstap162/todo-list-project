from django import forms

from todo.models import Task, Tag


class DateInput(forms.DateInput):
    input_type = "date"


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=DateInput()
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"
