from django.shortcuts import render

<<<<<<< HEAD
=======
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            #assign current user to the item

            new_item.user = request.user
            new_item.save()
            messages.success(request,'Image added successfully')
        else:
            # build form with data provided by the bookmarklet
            form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


>>>>>>> 8e3bbc298c7cf01864cb4331255237e751fe8a62
# Create your views here.
