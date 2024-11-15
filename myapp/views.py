from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import UseContactEmail, User
from .forms import UseContactEmailForm  # We'll create this form

# Create View
def create_email(request):
    if request.method == "POST":
        form = UseContactEmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("email_list")  # Redirect to the list view
    else:
        form = UseContactEmailForm()
    return render(request, "create_email.html", {"form": form})

# Read/List View
def email_list(request):
    emails = UseContactEmail.objects.all()
    return render(request, "email_list.html", {"emails": emails})

# Update View
def update_email(request, pk):
    email = get_object_or_404(UseContactEmail, pk=pk)
    if request.method == "POST":
        form = UseContactEmailForm(request.POST, instance=email)
        if form.is_valid():
            form.save()
            return redirect("email_list")
    else:
        form = UseContactEmailForm(instance=email)
    return render(request, "update_email.html", {"form": form})

# Delete View
def delete_email(request, pk):
    email = get_object_or_404(UseContactEmail, pk=pk)
    if request.method == "POST":
        email.delete()
        return redirect("email_list")
    return render(request, "delete_email.html", {"email": email})
