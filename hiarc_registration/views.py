from django.shortcuts import render, HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from .forms import HiarcUserCreationForm1, HiarcUserCreationForm2, HiarcUserCreationForm3
from .models import HiarcUser

class SignupWizard(SessionWizardView):
    
    template_name = 'hiarc_registration/register.html'
    form_list = [HiarcUserCreationForm1, HiarcUserCreationForm2, HiarcUserCreationForm3]
   
    def done(self, form_list, **kwargs):        
        if self.request.method == 'POST':            
            
            data = {}
            for form in form_list:
                data.update(form.cleaned_data)  

            user = HiarcUser.objects.create_user(**data)   
                 
        return render(self.request, 'hiarc_registration/done.html', {
            'form_data' : [form.cleaned_data for form in form_list],
        })
        
    