from django.shortcuts import redirect
from user_operations.form import CommentValiForm

# Create your views here.
def comment(request):
    url_source = request.META['HTTP_REFERER']
    comment_data = dict()
    product_id = request.POST.get('product',None)
    content = request.POST.get('content',None)
    comment_data['user'] = request.user.id
    comment_data['content'] = content
    comment_data['product'] = product_id
    data = CommentValiForm(comment_data)
    if not data.is_valid():
        return redirect(url_source)
    data.save()
    return redirect(url_source)