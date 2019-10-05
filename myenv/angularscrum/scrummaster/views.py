from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from scrummaster.models import ScrumyGoals
from scrummaster.serializers import ScrumyGoalsSerializer, UserSerializer



@csrf_exempt
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(scrumy_goal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method =='DELETE':
        user.delete()
        return HttpResponse(status=204)
    


@csrf_exempt
def scrumy_goals_list(request):

    if request.method == 'GET':
        scrumy_goals = ScrumyGoals.objects.all()
        serializer = ScrumyGoalsSerializer(scrumy_goals, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScrumyGoalsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def scrumy_goal_detail(request, pk):


    try:
        scrumy_goal = ScrumyGoals.objects.get(pk=pk)
    except ScrumyGoals.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ScrumyGoalsSerializer(scrumy_goal)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ScrumyGoalsSerializer(scrumy_goal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        scrumy_goal.delete()
        return HttpResponse(status=204)
