from django.shortcuts import render,redirect
from django.contrib import messages
from mail_templated import send_mail
from django.views.generic import ListView, FormView, TemplateView
from main.models import CompanyInfo
from main.forms import StudentForm
from django.template.loader import render_to_string

# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'


class CompanyProblemsList(ListView):
    template_name = 'main/problems_list.html'
    model = CompanyInfo
    context_object_name = 'problems'

def StudentFormView(request):
    form = StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.problem_statement_1 = form.cleaned_data['problem_statement_1']
            instance.problem_statement_2 = form.cleaned_data['problem_statement_2']
            instance.problem_statement_3 = form.cleaned_data['problem_statement_3']
            instance.problem_statement_4 = form.cleaned_data['problem_statement_4']
            email_address = form.cleaned_data['team_leader_email']
            print(email_address,form.cleaned_data['team_leader_name'])
            send_mail('email/confirmation.tpl',{'team_leader':form.cleaned_data['team_leader_name']},'vcet.hackathon@vcet.edu.in',[email_address,])
            instance.save()
            return redirect('index')
    return render(request,'main/form.html',{'form':form})

