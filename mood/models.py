from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy 😊'),
        ('Sad', 'Sad 😢'),
        ('Angry', 'Angry 😡'),
        ('Stressed', 'Stressed 😰'),
        ('Calm', 'Calm 😌'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    note = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.get_mood_display()} on {self.date.strftime('%Y-%m-%d')}"
