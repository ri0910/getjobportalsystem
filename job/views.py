from django.http import request
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from datetime import date

def index(request):
    return render(request, 'index.html')
def admin_login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'admin_login.html',d)
def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user=request.user
    nuser=Job_seeker.objects.get(user=user)
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        m=request.POST['mobile']
        e=request.POST['email']
        g=request.POST['gender']
        nuser.fname=f
        nuser.lname=l
        nuser.mobile=m
        nuser.gender=g
        nuser.email=e
        try:
           nuser.save()
           nuser.user.save()
           error="no"
        except:
            error="yes"
    d={'nuser':nuser,'error':error}
    return render(request,'user_home.html',d)
def Logout(request):
    logout(request)
    return redirect('index')
def company_signup(request):
    error=""
    if request.method=='POST':
        c=request.POST['companyname']
        con=request.POST['mobile']
        e=request.POST['email']
        p=request.POST['pwd']
        w=request.POST['website']
        try:
           user= User.objects.create_user(username=e,password=p)
           Company.objects.create(user=user,mobile=con,companyname=c,website=w,type="company",status="pending")
           error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'company_signup.html',d)
def user_login(request):
    error=""
    if request.method=="POST":
        u=request.POST['uname'];
        p=request.POST['pwd'];
        user=authenticate(username=u,password=p)
        if user:
            try:
                user1=Job_seeker.objects.get(user=user)
                if user1.type=="job-seeker":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d={'error':error}
    return render(request,'user_login.html',d)
def company_login(request):
    error=""
    if request.method=="POST":
        u=request.POST['uname'];
        p=request.POST['pwd'];
        user=authenticate(username=u,password=p)
        if user:
            try:
                user1=Company.objects.get(user=user)
                if user1.type=="company" and user1.status!="pending":
                    login(request,user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d={'error':error}
    return render(request,'company_login.html',d)
def user_signup(request):
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        c=request.POST['mobile']
        e=request.POST['email']
        p=request.POST['pwd']
        g=request.POST['gender']
        try:
           user= User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           Job_seeker.objects.create(user=user,mobile=c,gender=g,type="job-seeker")
           error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'user_signup.html',d)
def company_home(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    user=request.user
    company=Company.objects.get(user=user)
    error=""
    if request.method=='POST':
        com=request.POST['companyname']
        m=request.POST['mobile']
        e=request.POST['email']
        w=request.POST['website']
        company.companyname=com
        company.mobile=m
        company.website=w
        try:
           company.save()
           error="no"
        except:
            error="yes"
    d={'company':company,'error':error}
    return render(request,'company_home.html',d)
def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    ccount=Company.objects.all().count()
    jcount=Job_seeker.objects.all().count()
    d={'ccount':ccount,'jcount':jcount}
    return render(request,'admin_home.html',d)
def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Job_seeker.objects.all()
    d={'data':data}
    return render(request,'view_users.html',d)
def delete_users(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')
def company_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Company.objects.filter(status='pending')
    d={'data':data}
    return render(request,'company_pending.html',d)
def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    company=Company.objects.get(id=pid)
    if request.method=="POST":
        s=request.POST['status']
        company.status=s
        try:
            company.save()
            error="no"
        except:
            error="yes"
    d={'company':company,'error':error}
    return render(request,'change_status.html',d)
def company_accept(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Company.objects.filter(status='Accept')
    d={'data':data}
    return render(request,'company_accept.html',d)
def company_reject(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Company.objects.filter(status='Reject')
    d={'data':data}
    return render(request,'company_reject.html',d)
def company_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Company.objects.all()
    d={'data':data}
    return render(request,'company_all.html',d)
def delete_company(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('company_all')
def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method=="POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={'error':error}
    return render(request,'change_passwordadmin.html',d) 
def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={'error':error}
    return render(request,'change_passworduser.html',d)
def change_passwordcompany(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    error=""
    if request.method=="POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d={'error':error}
    return render(request,'change_passwordcompany.html',d)  
def add_job(request):
    if not request.user.is_authenticated:
        return redirect("company_login")
    error=""
    if request.method=='POST':
        d=request.POST['department']
        j=request.POST['job_role']
        e=request.POST['experience']
        l=request.POST['location']
        s=request.POST['salary']
        sk=request.POST['required_skills']
        st=request.POST['start_date']
        ed=request.POST['end_date']
        des=request.POST['description']
        user=request.user
        user=Company.objects.get(user=user)
        try:
           Job.objects.create(company=user,start_date=st,end_date=ed,department=d,job_role=j,experience=e,location=l,salary=s,required_skills=sk,description=des,creation_date=date.today())
           error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_job.html',d)  
def job_list(request):
    if not request.user.is_authenticated:
        return redirect("company_login")
    user=request.user
    company=Company.objects.get(user=user)
    job=Job.objects.filter(company=company) 
    d={'job':job}
    return render(request,'job_list.html',d)    
def edit_jobdetails(request,pid):
    if not request.user.is_authenticated:
        return redirect("company_login")
    error=""
    job=Job.objects.get(id=pid)
    if request.method=='POST':
        d=request.POST['department']
        j=request.POST['job_role']
        e=request.POST['experience']
        l=request.POST['location']
        s=request.POST['salary']
        sk=request.POST['required_skills']
        st=request.POST['start_date']
        ed=request.POST['end_date']
        des=request.POST['description']
        
        job.department=d
        job.job_role=j
        job.experience=e
        job.location=l
        job.salary=s
        job.required_skills=sk
        job.description=des
        
        if st:
            try:
                job.start_date=st
            except:
                pass
        else:
            pass
        if ed:
            try:
                job.end_date=ed
            except:
                pass
        else:
            pass
        try:
            job.save()
            error="no"
        except:
            error="yes"
            
    d={'error':error,'job':job}
    return render(request,'edit_jobdetails.html',d)   
def latest_job(request):
    job=Job.objects.all().order_by('-start_date')
    d={'job':job}
    return render(request,'latest_job.html',d) 
def user_latestjob(request):
    job=Job.objects.all().order_by('-start_date')
    d={'job':job}
    return render(request,'user_latestjob.html',d) 
def user_latestjob(request):
    job=Job.objects.all().order_by('-start_date')
    user=request.user
    job_seeker=Job_seeker.objects.get(user=user)
    data=Apply.objects.filter(job_seeker=job_seeker)
    li=[]
    for i in data:
        li.append(i.job.id)
    d={'job':job,'li':li}
    return render(request,'user_latestjob.html',d) 
def job_details(request,pid):
    job=Job.objects.get(id=pid)
    d={'job':job}
    return render(request,'job_details.html',d)
def applyforjob(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user=request.user
    job_seeker=Job_seeker.objects.get(user=user)
    job=Job.objects.get(id=pid)
    date1=date.today()
    if job.end_date<date1:
        error="close"
    elif job.start_date>date1:
        error="notopen"
    else:
        if request.method=='POST':
            r=request.FILES['resume']
            Apply.objects.create(job=job,job_seeker=job_seeker,resume=r,apply_date=date.today())
            error="done"
    d={'error':error}
    return render(request,'applyforjob.html',d)
def applied_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    data=Apply.objects.all()
    d={'data':data}
    return render(request,'applied_candidatelist.html',d)
def delete_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('company_login')
    user=Job.objects.get(id=pid)
    user.delete()
    return redirect('job_list')
def delete_candidate(request,pid):
    if not request.user.is_authenticated:
        return redirect('company_login')
    user=Apply.objects.get(id=pid)
    user.delete()
    return redirect('applied_candidatelist')

