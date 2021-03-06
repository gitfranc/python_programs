from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    ''' Register new account '''

    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)


        if form.is_valid():
            new_user = form.save()
            # new account login automaticly, and go to homepage
            login(request, new_user)
            return redirect("learning_notes_apps:index")

    # Display empty form or invaild form
    context = {"form": form}
    return render(request, "registration/register.html", context)
