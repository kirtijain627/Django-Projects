from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistrtion
from .models import User
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = UserRegistrtion(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']

            user1 = User(name=nm, email=em, password=pw)
            user1.save()
            fm = UserRegistrtion()
            
            # fm.save()      #second methdo

    else:
        fm = UserRegistrtion()
    stud = User.objects.all()

    
    return render(request, 'crud/add_and_show.html', {'form':fm, 'stu':stud})

#for deleting an item

def delete_data(request, id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        
        return HttpResponseRedirect('/')


#for editing and updating data
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserRegistrtion(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserRegistrtion(instance=pi)

    return render(request, 'crud/update_student.html', {'form':fm})


def learn_django(request):
    student = {'names': ['Kirti', 'Aditya', 'Saurav', 'Kanwar']}
    return render(request, 'crud/courseone.html', student)