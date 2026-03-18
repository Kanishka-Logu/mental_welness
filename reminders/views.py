from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reminder
from .forms import ReminderForm

@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'reminders/list.html', {'reminders': reminders})

@login_required
def reminder_create(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminders/form.html', {'form': form})

@login_required
def reminder_toggle(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
    reminder.is_active = not reminder.is_active
    reminder.save()
    return redirect('reminder_list')

@login_required
def reminder_delete(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
    reminder.delete()
    return redirect('reminder_list')
