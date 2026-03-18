from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MoodEntry
from .forms import MoodEntryForm
from reportlab.pdfgen import canvas
from io import BytesIO

@login_required
def log_mood(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return redirect('dashboard')
    else:
        form = MoodEntryForm()
    return render(request, 'mood/log_mood.html', {'form': form})

@login_required
def mood_history(request):
    moods = MoodEntry.objects.filter(user=request.user)
    return render(request, 'mood/history.html', {'moods': moods})

@login_required
def export_mood_pdf(request):
    moods = MoodEntry.objects.filter(user=request.user)
    
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    
    p.drawString(100, 800, f"Mood History Report - {request.user.username}")
    
    y = 750
    for mood in moods:
        p.drawString(100, y, f"{mood.date.strftime('%Y-%m-%d %H:%M')} - {mood.get_mood_display()}")
        if mood.note:
            y -= 20
            p.drawString(120, y, f"Note: {mood.note[:50]}...")
        y -= 30
        
        if y < 50:
            p.showPage()
            y = 750
            
    p.showPage()
    p.save()
    
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mood_report.pdf"'
    return response
