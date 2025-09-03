from django.core.management.base import BaseCommand
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **options):
        # Users
        User.objects.create(email='alice@example.com', name='Alice', password='password123')
        User.objects.create(email='bob@example.com', name='Bob', password='password123')
        User.objects.create(email='carol@example.com', name='Carol', password='password123')

        # Teams
        Team.objects.create(name='Team Alpha', members=['alice@example.com', 'bob@example.com'])
        Team.objects.create(name='Team Beta', members=['carol@example.com'])

        # Activities
        Activity.objects.create(user='alice@example.com', activity_type='run', duration=30, timestamp='2025-09-01T10:00:00Z')
        Activity.objects.create(user='bob@example.com', activity_type='walk', duration=45, timestamp='2025-09-01T11:00:00Z')
        Activity.objects.create(user='carol@example.com', activity_type='cycle', duration=60, timestamp='2025-09-01T12:00:00Z')

        # Leaderboard
        Leaderboard.objects.create(team='Team Alpha', score=75)
        Leaderboard.objects.create(team='Team Beta', score=60)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')
        Workout.objects.create(name='Squats', description='Do 40 squats')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
