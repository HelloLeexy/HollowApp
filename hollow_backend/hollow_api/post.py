from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from datetime import datetime
from hollow_api.models import Post  # 假设您有一个名为 Post 的模型
from hollow_api.models import CustomUser
@require_POST
def create_post(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('userID')
        user_instance = CustomUser.objects.get(user_id=user_id)
        # 创建帖子
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        post = Post.objects.create(
            poster=user_instance,
            title=data.get('title'),
            classification = data.get('region'),
            content=data.get('desc'),
            publish_date = formatted_time,
        )

        # 处理创建帖子的逻辑
        post.save()

        return JsonResponse({'success': True, 'message': 'Post created successfully'})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
