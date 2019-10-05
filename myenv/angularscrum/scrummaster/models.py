from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GoalStatus(models.Model):
    status_name=models.CharField(max_length=20)

class ScrumyGoals(models.Model):
    goal_name=models.CharField(max_length=20)
    goal_id=models.CharField(max_length=20)
    created_by=models.CharField(max_length=20)
    moved_by=models.CharField(max_length=20)
    owner=models.CharField(max_length=20)
    goal_status=models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user=models.ForeignKey(User, related_name='scrummaster', on_delete=models.CASCADE)

class ScrumHistroy(models.Model):
    moved_by=models.CharField(max_length=20)
    created_by=models.CharField(max_length=20)
    moved_from=models.CharField(max_length=20)
    moved_to=models.CharField(max_length=20)
    time_of_action=models.DateTimeField(max_length=20)
    goal=models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)