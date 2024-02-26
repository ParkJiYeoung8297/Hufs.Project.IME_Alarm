from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Post

class Main(APIView):
    def get(self,request):
        post_list=Post.objects.all()
        #for post in post_list:
        #    print(post.title)
        return render(request,"Alarm/main.html",context=dict(posts=post_list))
    

