from django.shortcuts import render, HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from .forms import HiarcUserCreationForm1, HiarcUserCreationForm2, HiarcUserCreationForm3

# Create your views here.

class SignupWizard(SessionWizardView):

    template_name = 'hiarcex/registration.html'
    form_list = [HiarcUserCreationForm1, HiarcUserCreationForm2, HiarcUserCreationForm3]
    
    def done(self, form_list, **kwargs):           
        return render(self.request, 'hiarcex/done.html', {
            'form_data' : [form.cleaned_data for form in form_list],
        })
