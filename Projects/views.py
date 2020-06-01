from django.shortcuts import render

def project(request):
    return render(request,'Projects/projectlist.html',{'title': 'MenInTheMiddleAttack'})

def mitmdoit(request):
     return render(request,'Projects/mitmdoit.html',{'title': 'MenInTheMiddleAttack'})
