from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        user_id = user.user_id  # 获取用户ID
        return JsonResponse({'success': True, 'message': 'Login successful', 'userID': user_id})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid username or password'})
