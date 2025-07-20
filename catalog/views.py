from django.shortcuts import render

# catalog/views.py

from django.shortcuts import render


def home(request):

    return render(request, 'home.html')


def contacts(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Новое сообщение от пользователя {name} (email: {email}): {message}")

        context = {
            'success': True
        }

        return render(request, 'contacts.html', context)

    return render(request, 'contacts.html')
