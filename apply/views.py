from django.shortcuts import render, redirect
from .models import Apply

# Create your views here.
def main(request):
    return render(request, 'main.html')

def apply(request):
    return render(request, 'apply.html')

def create(request):
    new_apply = Apply()

    new_apply.name = request.POST['name']
    new_apply.studentId = request.POST['studentId']
    new_apply.grade = request.POST['grade']
    new_apply.major = request.POST['major']
    new_apply.email = request.POST['email']
    new_apply.phone = request.POST['phone']

    new_apply.motive = request.POST['motive']
    new_apply.position = request.POST['position']
    new_apply.positionRe = request.POST['positionRe']
    new_apply.teamwork = request.POST['teamwork']
    new_apply.passion = request.POST['passion']
    new_apply.code = request.POST['code']

    new_apply.save()
    return redirect('thankyou')

def thankyou(request):
    return render(request, 'thankyou.html')