from django.shortcuts import render

# Create your views here.
def chatroom(request):
    content = request.id
    return render(request, "chatroom.html");