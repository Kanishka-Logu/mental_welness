from django.db import models

class Suggestion(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy 😊'),
        ('Sad', 'Sad 😢'),
        ('Angry', 'Angry 😡'),
        ('Stressed', 'Stressed 😰'),
        ('Calm', 'Calm 😌'),
    ]

    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    text = models.TextField()

    def __str__(self):
        return f"Suggestion for {self.get_mood_display()}"
