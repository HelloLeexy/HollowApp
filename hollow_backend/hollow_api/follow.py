from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import CustomUser, Follow
import json
@require_POST
def follow_user(request):
    try:
        data = json.loads(request.body)# Assuming data is sent as form data
        user_id = data.get('userID')
        poster_id = data.get('posterID')
        # 获取对应的用户对象
        follower = CustomUser.objects.get(user_id=user_id)
        followed = CustomUser.objects.get(user_id=poster_id)

        # 检查是否已经存在关注关系
        existing_follow = Follow.objects.filter(follower=follower, followed=followed).exists()

        if not existing_follow:
            # 创建关注关系
            follow = Follow.objects.create(follower=follower, followed=followed)
            follow.save()
            return JsonResponse({'success': True, 'message': f'You are now following {followed.username}.'})
        else:
            return JsonResponse({'success': False, 'message': 'You are already following this user.'})
    except Exception as e:
        # 记录错误日志
        print(f'Error following user: {str(e)}')
        return JsonResponse({'success': False, 'message': 'Error following user'})
