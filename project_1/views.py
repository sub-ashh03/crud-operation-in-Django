from django.shortcuts import render,redirect
from .forms import *
from .models import *



def ADD_form_2(request):

    context = {
        'productform_3': ADD_form()
        }
    return render(request,'form.html',context)


def homepage(request):
    data=studentData.objects.all()
    print(data)
    context={"data":data}
    return render(request, 'index.html',context)



def insertData(request):
    if request.method =="POST":
        name=request.POST.get('name')
        mail=request.POST.get('mail')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,mail,age,gender)
        query=studentData(name=name,mail=mail,age=age,gender=gender)
        query.save()
        return redirect("/")

    # Data = studentData.objects.all()
    # context = {"data": Data}
    return render (request,'index.html')

def updateData(request,id):
    if request.method =="POST":
        name=request.POST['name']
        mail=request.POST['mail']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=studentData.objects.get(id=id)
        edit.name=name
        edit.mail=mail
        edit.age=age
        edit.gender=gender
        edit.save()
    
        return redirect("/")
    
    d=studentData.objects.get(id=id)
    context={"d":d}
    return render(request,'edit.html',context)

def deleteData(request,id):
    d=studentData.objects.get(id=id)
    d.delete()
    return redirect("/")