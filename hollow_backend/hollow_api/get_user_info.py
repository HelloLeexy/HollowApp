from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from hollow_api.models import CustomUser

@require_POST
def get_user(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('userID')
        user_instance = CustomUser.objects.get(user_id=user_id)
        # 手动转换模型数据为 JSON 格式
        user_data = {
            'username': user_instance.username,
            'user_id': user_instance.user_id,
            'programme': user_instance.programme,
            'dob': user_instance.dob,
            'age': user_instance.age,
            'yearOfStudy': user_instance.yearOfStudy,
            'aboutMe': user_instance.aboutMe,
            'img': user_instance.img,
        }
        # 返回 JSON 响应
        return JsonResponse({'success': True, 'users': [user_data]})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
