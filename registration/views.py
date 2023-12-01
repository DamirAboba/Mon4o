from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Cabinet, UserActivity
import pytz


def combined_view(request):
    cabinets = Cabinet.objects.filter(is_occupied=False)
    user_activities = UserActivity.objects.filter(end_time__isnull=True)
    active_cabinets = Cabinet.objects.filter(is_occupied=True)

    if request.method == 'POST':
        if 'register_action' in request.POST:
            selected_cabinet_number = int(request.POST.get('cabinet_number'))
            selected_cabinet = Cabinet.objects.get(number=selected_cabinet_number)
            if not selected_cabinet.is_occupied:
                selected_cabinet.is_occupied = True
                selected_cabinet.save()
                UserActivity.objects.create(cabinet=selected_cabinet)

        elif 'checkout_action' in request.POST:
            activity_id = int(request.POST.get('activity_id'))
            activity = UserActivity.objects.get(id=activity_id, end_time__isnull=True)
            local_tz = pytz.timezone("Asia/Bishkek")
            end_time = timezone.now().astimezone(local_tz)
            activity.end_time = end_time

            # Расчет суммы
            activity.amount = calculate_amount(activity.start_time, end_time)
            activity.save()
            cabinet = activity.cabinet
            cabinet.is_occupied = False
            cabinet.save()

    context = {
        'cabinets': cabinets,
        'user_activities': user_activities,
        'active_cabinets': active_cabinets,
    }
    return render(request, 'registration/combined.html', context)



def calculate_amount(start_time, end_time):
    duration = end_time - start_time
    total_minutes = duration.total_seconds() / 60

    if total_minutes <= 2:
        return 500.0
    else:
        additional_minutes = total_minutes - 2
        return 500.0 + (additional_minutes * 60)

