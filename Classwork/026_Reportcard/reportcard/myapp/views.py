from django.shortcuts import render,redirect
from myapp.models import *
from django.core.paginator import Paginator
from django.db.models import Sum,Count,Q
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Create your views here.

def index(request):
    students = Student.objects.all()
    paginator = Paginator(students,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"students":page_obj})

def report(request):
    id = request.GET['id']
    action = request.GET['action']
    data = Marks.objects.filter(student_id=id)
    
    all = Student.objects.annotate(
    total_marks=Sum('marks__marks'),
    failed_subjects=Count(
        'marks',
        filter=Q(marks__marks__lt=36)
    )
    ).filter(
        failed_subjects=0
    ).order_by('-total_marks')
        
    rank=1
    k = 0
    for i in all :       
        if i.id==int(id):
            k=1
            break
        rank+=1
    if k==0 :
        rank=0
    total = 0
    flag = 'PASS'
    for i in data:
        total+=i.marks
        if i.marks<36:
            flag="FAIL"
            
    per = round((total*100)/700,2)
   
    if action=='display':
        return render(request,"report.html",{"data":data,"total":total,"per":per,"flag":flag,"rank":rank})
    else:
        html_message = render_to_string(
        "report.html",{"data":data,"total":total,"per":per,"flag":flag,"rank":rank}
         )

        email = EmailMultiAlternatives(
            subject="Report Card",
            body="Attachment report card",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["ankitpatel8085@gmail.com"]
        )

        email.attach_alternative(html_message, "text/html")
        email.send()
        return redirect("index")

