from django.shortcuts import render,redirect
from django.contrib import messages
from mail_templated import send_mail
from django.views.generic import ListView, FormView, TemplateView
from main.models import CompanyInfo
from main.forms import StudentForm,Email
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
            messages.success(request,'Thanks ! for applying . You\'ll be notified about further steps.')
            instance.save()
            send_email(email_address)
            return redirect('/')
    return render(request,'main/form.html',{'form':form})

def test_email(request):
    form = Email()
    if request.method == 'POST':
        form = Email(request.POST)
        if form.is_valid():
            to = form.cleaned_data['email_id']
            send_mail('email/confirmation.tpl',{'team_leader':'Ravi'},'ravi@gmail.com',[to,])
    return render(request,'main/email.html',{'form':form})

def send_email(to_email):
        subject = 'cool'
        content = 'cm'
        from_email = 'onecourse1@gmail.com'

        send_mail(subject,
        content,
        from_email,
        [to_email],
        fail_silently=False
        )
        