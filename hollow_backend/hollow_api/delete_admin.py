from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Post  # 请替换为你实际的 Post 模型
import json
@csrf_exempt  # 为了简化示例，这里使用了禁用 CSRF 保护，请根据实际需求添加 CSRF 保护
@require_POST
def admin_delete_post(request):
    try:
        # 获取前端传递的 postID
        post_id = json.loads(request.body).get('postID')

        # 在这里添加删除 post 的逻辑，假设你的 Post 模型有一个名为 id 的字段
        Post.objects.filter(id=post_id).delete()

        # 返回成功的响应
        return JsonResponse({'success': True, 'message': 'Post deleted successfully'})
    except Exception as e:
        # 如果发生错误，返回错误的响应
        return JsonResponse({'success': False, 'message': str(e)})
