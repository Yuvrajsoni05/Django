from django.shortcuts import render, redirect
from .models import AllModel


def example_view(request):
    all_data = AllModel.objects.all()  # Fetch all entries from the database

    if request.method == 'POST':
        # Get data from POST request
        name = request.POST.get('name')
        description = request.POST.get('description')
        age = request.POST.get('age')
        price = request.POST.get('price')
        is_active = request.POST.get('is_active') == 'on'
        birth_date = request.POST.get('birth_date')
        event_time = request.POST.get('event_time')
        file = request.FILES.get('file')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        website = request.POST.get('website')
        favorite_color = request.POST.get('favorite_color')

        # Save data to the model
        example = AllModel(
            name=name,
            description=description,
            age=age,
            price=price,
            is_active=is_active,
            birth_date=birth_date,
            event_time=event_time,
            file=file,
            image=image,
            email=email,
            website=website,
            favorite_color=favorite_color,
        )
        example.save()

        print(f"Data saved: {example}")  # Debug: check if data is saved
        return redirect('success')  # Redirect to avoid re-posting on refresh

    print(f"All Data: {all_data}")  # Debug: check if data is being passed
    return render(request, 'index.html', {'all': all_data})


def success_view(request):
    return render(request, 'success.html')
