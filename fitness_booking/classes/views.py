from django.shortcuts import render, get_object_or_404, redirect
from .models import FitnessClass, Booking

def class_list(request):
    classes = FitnessClass.objects.all()
    return render(request, 'classes/class_list.html', {'classes': classes})

def book_class(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    # Replace request.user with a placeholder for now since no login is required
    if Booking.objects.filter(fitness_class=fitness_class).count() < fitness_class.max_participants:
        booking = Booking.objects.create(user=None, fitness_class=fitness_class)
        return redirect('class_list')
    else:
        return render(request, 'classes/full_class.html')

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('profile')

def profile(request):
    bookings = Booking.objects.all()  # Show all bookings since there's no user filter
    return render(request, 'classes/profile.html', {'bookings': bookings})

def class_detail(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    participants = Booking.objects.filter(fitness_class=fitness_class)
    return render(request, 'classes/class_detail.html', {'class': fitness_class, 'participants': participants})

from django.shortcuts import render
from .models import FitnessClass, Booking

from django.shortcuts import render
from .models import FitnessClass, Booking

def public_profile(request):
    classes = FitnessClass.objects.all()
    bookings = Booking.objects.all()  # Fetch all bookings to display
    context = {
        'classes': classes,
        'bookings': bookings,
    }
    return render(request, 'classes/public_profile.html', context)

