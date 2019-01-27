from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import password_validation
from .models import HiarcUser, STATUSES, MAJORS, SEMESTERS

import json
# import request

class HiarcUserCreationForm1(forms.Form):
    
    # 1
    email = forms.EmailField(required=True)
    real_name = forms.CharField(required=True, max_length=20, help_text='실제 이름을 입력해주세요')
    username = forms.CharField(required=True, max_length=20, help_text='user로 등록할 이름을 입력해주세요')    
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput        
    )    
    student_id = forms.CharField(required=True, max_length=7) # validator
    phone_number = forms.CharField(required=True, max_length=20)
    status = forms.CharField(required=True, widget=forms.Select(choices=STATUSES))
    semester = forms.CharField(required=True, widget=forms.Select(choices=SEMESTERS))
    major  = forms.CharField(required=True, widget=forms.Select(choices=MAJORS))
    minor  = forms.CharField(required=True, widget=forms.Select(choices=MAJORS))

    


    class Meta:
        model = HiarcUser
        fields = ("email", "real_name", "username", "student_id", "phone_number", "status", "semester", "major", "minor")

    def save(self, commit=True):
        user = super(HiarcUserCreationForm1, self).save(commit=False)

        user.email = self.cleaned_data["email"]
        first_name, last_name = self.cleaned_data["username"].split()
        user.first_name = first_name
        user.last_name = last_name             
        user.student_id = self.cleaned_data["student_id"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.status = self.cleaned_data["status"]
        user.semester = self.cleaned_data["semester"]        
        user.major = self.cleaned_data["major"]
        user.minor = self.cleaned_data["minor"]
        '''
        webhook_url = system.environment['SLACK_WEBHOOK_URL']
        message = "회원가입 신청이 들어왔습니다. \n이름 : {}\n 이메일 : {} \n학과/학번/학년 : {}\n 자세한 사항은 관리자페이지에서 확인해보세요.".format(user.real_name, user.email, user.status)
        slack_data = { "text": message, "color": "#FAA3E3"} 

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        # '''

        # if commit:
        #     user.save()
        # return user

class HiarcUserCreationForm2(forms.Form):

    # 2 
    motivation = forms.CharField(required=True, widget=forms.Textarea)
    portfolio = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = HiarcUser
        fields = ("motivation", "portfolio", "comment")

    def save(self, commit=True):
        user = super(HiarcUserCreationForm2, self).save(commit=False)

        user.motivation = self.cleaned_data["motivation"]
        user.portfolio = self.cleaned_data["portfolio"]
        user.comment = self.cleaned_data["comment"]

        '''
        webhook_url = system.environment['SLACK_WEBHOOK_URL']
        message = "회원가입 신청이 들어왔습니다. \n이름 : {}\n 이메일 : {} \n학과/학번/학년 : {}\n 자세한 사항은 관리자페이지에서 확인해보세요.".format(user.real_name, user.email, user.status)
        slack_data = { "text": message, "color": "#FAA3E3"} 

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        '''

        # if commit:
        #     user.save()
        # return user

class HiarcUserCreationForm3(forms.Form):

    # 3
    codeforces_id = forms.CharField(required=False, widget=forms.Textarea)
    boj_id = forms.CharField(required=False, widget=forms.Textarea)
    topcoder_id = forms.CharField(required=False, widget=forms.Textarea)
    github_id = forms.CharField(required=False, widget=forms.Textarea)
    blog_url = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = HiarcUser
        fields = ("codeforces_id", "boj_id", "topcoder_id", "github_id", "blog_url")

    def save(self, commit=True):
        user = super(HiarcUserCreationForm3, self).save(commit=False)

        user.codeforces_id = self.cleaned_data["coedforces_id"]
        user.boj_id = self.cleaned_data["boj_id"]
        user.topcoder_id = self.cleaned_data["topcoder_id"]
        user.gihub_id = self.cleaned_data["github_id"]
        user.blog_url = self.cleaned_data["blog_url"]
            
        # if commit:
        #     user.save()
        #     return user