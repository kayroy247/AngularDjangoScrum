from rest_framework import serializers
from scrummaster.models import ScrumyGoals
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'groups']

class ScrumyGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'goal_id', 'created_by', 'moved_by', 'owner', 'goal_status', 'user' ]