from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mood.models import MoodEntry
from journal.models import JournalEntry
from .models import Suggestion

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'dashboard/home.html')

@login_required
def dashboard(request):
    moods = MoodEntry.objects.filter(user=request.user).order_by('date')
    recent_moods = MoodEntry.objects.filter(user=request.user).order_by('-date')[:7]
    journals = JournalEntry.objects.filter(user=request.user).order_by('-date')[:5]
    
    suggestions = []
    if recent_moods:
        latest_mood = recent_moods[0].mood
        suggestions = Suggestion.objects.filter(mood=latest_mood)
    
    # Prepare data for chart
    labels = [mood.date.strftime('%b %d') for mood in moods]
    
    mood_scoring = {
        'Happy': 5,
        'Calm': 4,
        'Sad': 2,
        'Stressed': 2,
        'Angry': 1,
    }
    data = [mood_scoring.get(mood.mood, 3) for mood in moods]

    context = {
        'recent_moods': recent_moods,
        'journals': journals,
        'suggestions': suggestions,
        'labels': labels,
        'data': data
    }
    return render(request, 'dashboard/dashboard.html', context)

def wellness(request):
    return render(request, 'dashboard/wellness.html')
