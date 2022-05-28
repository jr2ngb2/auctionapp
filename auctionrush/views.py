#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("/")
            # return HttpResponseRedirect(reverse('auctions'))
        else:
            # for msg in form.error_messages:
            #     # print(form.error_messages[msg])
            #     print(msg)
            #     error_messages = form.error_messages[msg]

            return render(request = request,
                          template_name = "registration/register.html",
                          context={
                              "form": form,
                              "error_message": error_message,
                          })

    form = UserCreationForm
    return render(request = request,
                  template_name = "registration/register.html",
                  context={"form":form})

def success(request):
    return render(request , 'successPage.html')
