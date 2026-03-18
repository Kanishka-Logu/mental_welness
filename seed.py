import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mindtrack.settings')
django.setup()

from dashboard.models import Suggestion

def populate():
    suggestions = [
        ('Happy', 'Keep up the momentum! Share your positivity with a friend.'),
        ('Happy', 'Great time to start a new creative project.'),
        ('Sad', 'Allow yourself to feel this way. Consider journaling your thoughts.'),
        ('Sad', 'Reach out to someone you trust or try a short, gentle walk.'),
        ('Angry', 'Try a 5-minute deep breathing exercise to center yourself.'),
        ('Angry', 'Write down what made you angry, then rip up the paper as a release.'),
        ('Stressed', 'Take a break and listen to some calming music.'),
        ('Stressed', 'Try the 4-7-8 breathing exercise in the Wellness Hub.'),
        ('Calm', 'A perfect moment for a short meditation or mindfulness practice.'),
        ('Calm', 'Maintain this peace by doing something you love today.'),
    ]
    
    for mood, text in suggestions:
        Suggestion.objects.get_or_create(mood=mood, text=text)
    
    print("Database successfully populated with smart suggestions.")

if __name__ == '__main__':
    populate()
