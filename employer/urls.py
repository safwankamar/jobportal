
from django.urls import path
from employer import views

urlpatterns = [
path('home',views.EmployerHomeView.as_view(),name='home'),
    path('jobs/add',views.AddJobView.as_view(),name='emp-addjob'),
    path('jobs/all',views.ListJobView.as_view(),name='all-jobs'),
    path('jobs/details/<int:id>',views.JobDetailView.as_view(),name='job-details'),
    path('jobs/change/<int:id>',views.JobEditView.as_view(),name='job-changes'),
    path('jobs/remove/<int:id>',views.JobDeleteView.as_view(),name='job-delete'),
    path('user/account/signup',views.Signupview.as_view(),name='signup'),
    path('user/account/signin',views.SigninView.as_view(),name='signin'),
    path('user/account/signout',views.signout_view,name='signout'),
    path('user/password/changepassword',views.ChangePasswordView.as_view(),name='changepassword'),
    path('user/password/passwordreset',views.PasswordResetView.as_view(),name='resetpassword'),

]