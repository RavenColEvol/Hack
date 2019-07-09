from django import forms
from main import models

def getChoices():
    return tuple(models.CompanyInfo.objects.values_list('company_problem_statement','company_problem_statement'))

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        problem_list = getChoices()
        self.fields['problem_statement_1'].choices = problem_list
        self.fields['problem_statement_2'].choices = problem_list
        self.fields['problem_statement_3'].choices = problem_list
        self.fields['problem_statement_4'].choices = problem_list
    
    problem_statement_1 = forms.ChoiceField()
    problem_statement_2 = forms.ChoiceField()
    problem_statement_3 = forms.ChoiceField()
    problem_statement_4 = forms.ChoiceField()
    class Meta:
        model = models.StudentForm
        fields = '__all__'

    def clean(self):
        cleaned_data  = super(StudentForm,self).clean()
        p1 = cleaned_data.get('problem_statement_1')
        p2 = cleaned_data.get('problem_statement_2')
        p3 = cleaned_data.get('problem_statement_3')
        p4 = cleaned_data.get('problem_statement_4')

        if (p1==p2 or p1==p3) or (p1==p4) or (p2==p3 or p2==p4) or p3==p4:
            raise forms.ValidationError('All four problem statement must be different')

        return self.cleaned_data

class Email(forms.Form):
    email_id = forms.CharField()