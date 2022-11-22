from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def account(request):
    return render(request, "account.html")

def post_history(request):
    return render(request, "post-history.html")

def create_post(request):
    return render(request, "create-a-post.html")

def post_in_my_area(request):
    return render(request, "posts-in-my-area.html")
