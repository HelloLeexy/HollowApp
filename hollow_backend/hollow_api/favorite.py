from django.http import JsonResponse
from django.views.decorators.http import require_POST
from hollow_api.models import Favorite, Post, CustomUser
import json

@require_POST
def add_favorite(request):
    try:
        # 解析前端传递的 JSON 数据
        data = json.loads(request.body)

        # 获取用户和帖子的ID
        user_id = data.get('user_id')
        post_id = data.get('post_id')

        # 获取用户和帖子实例
        user_instance = CustomUser.objects.get(user_id=user_id)
        post_instance = Post.objects.get(id=post_id)

        # 检查是否已经是收藏
        favorite_exists = Favorite.objects.filter(user=user_instance, post=post_instance).exists()

        if favorite_exists:
            # 如果已经收藏，取消收藏
            Favorite.objects.filter(user=user_instance, post=post_instance).delete()
            return JsonResponse({'success': True, 'message': 'Favorite removed successfully'})
        else:
            # 如果未收藏，添加收藏
            favorite = Favorite.objects.create(
                user=user_instance,
                post=post_instance,
            )
            favorite.save()
            return JsonResponse({'success': True, 'message': 'Favorite added successfully'})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
