from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView ,DeleteView,FormView,TemplateView
from employer.forms import JobForm
from employer.models import Jobs
from django.urls import reverse_lazy
from employer.forms import SignUpForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class EmployerHomeView(View):
    def get(self,request):
        return render(request,'emphome.html')


class AddJobView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp-addjob.html'
    success_url = reverse_lazy('all-jobs')

    # def get(self,request):
    #     form=JobForm()
    #     return render(request,'emp-addjob.html',{'form':form})
    # def post(self,request):
    #     form=JobForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,'emphome.html')
    #     else:
    #         return render(request,'emp-addjob.html',{'form':form})

class ListJobView(ListView):
    model=Jobs
    context_object_name='jobs'
    template_name='emp-listjob.html'
    # def get(self,request):
    #     qs=Jobs.objects.all()
    #     return render(request,'emp-listjob.html',{'jobs':qs})

class JobDetailView(DetailView):
    model = Jobs
    context_object_name = 'job'
    template_name = 'jobdetails.html'
    pk_url_kwarg = 'id'


    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,'jobdetails.html',{'job':qs})

class JobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp-editjob.html'
    success_url = reverse_lazy('all-jobs')
    pk_url_kwarg = 'id'

    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(instance=qs)
    #     return render(request,'emp-editjob.html',{'form':form})
    # def post(self,request,id):
    #     qs = Jobs.objects.get(id=id)
    #     form=JobForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('all-jobs')
    #     else:
    #         return render(request,'emp-editjob.html',{'form':form})

class JobDeleteView(DeleteView):
    model = Jobs
    success_url = reverse_lazy('all-jobs')
    template_name = 'emp-delete.html'
    pk_url_kwarg = 'id'


    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     qs.delete()
    #     return redirect('all-jobs')

class Signupview(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'usersignup.html'
    success_url = reverse_lazy('all-jobs')

class SigninView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            unname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            user=authenticate(request,username=unname,password=pwd)
            if user:
                login(request,user)
                return redirect('all-jobs')
            else:
                return render(request,'login.html',{'form':form})


def signout_view(request,*args,**kwargs):
    return redirect('signin')

class ChangePasswordView(TemplateView):
    template_name = 'changepassword.html'

    def post(self,request,*args,**kwargs):
        password=request.POST.get('password')
        username=request.user
        user=authenticate(request,username=username,password=password)
        if user:
            return redirect('resetpassword')
        else:
            return render(request,self.template_name)


class PasswordResetView(TemplateView):
    template_name = 'passwordreset.html'
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("password1")
        pwd2=request.POST.get("password2")
        if pwd1!=pwd2:
            return render (request,self.template_name,{"msg":"password incorrect"})
        else:
            U=User.objects.get(username=request.user)
            U.set_password(pwd1)
            U.save()
            return redirect("signin")



