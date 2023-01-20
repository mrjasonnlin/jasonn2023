from django.shortcuts import render

from upload_profile.models import Photo


# Create your views here.
def upload_profile(request):
    """
    Render the main page
    """
    context = {'like': 'Django 很棒'}
    return render(request, 'upload_profile/upload_profile.html', context)


def add(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')  # 對應剛剛add.html 中的input name
        user_img = request.FILES.get('user_image')
        introduce = request.FILES.get('introduce')
        user = Photo(user_name=user_name, user_image=user_img, introduce=introduce)
        user.save()
    return render(request, 'upload_profile/add.html', locals())


def detail(request):
    list_user = Photo.objects.all()  # 把資料庫中所有的user資料全部撈出來
    return render(request, 'upload_profile/detail.html', locals())
