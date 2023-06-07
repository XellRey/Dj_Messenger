from django.shortcuts import render, redirect
from .forms import MessageForm
from account.forms import AddToContact
from .models import Message
from django.db.models import Q

from account.models import CustomUser
# Create your views here.


def home_view(request):
    return render(request, 'djmessenger/homepage.html')


def chat_view(request):
    # Search
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        user_list = CustomUser.objects.filter(search)
    else:
        user_list = CustomUser.objects.all()

    data = {
        'user_list': user_list,
    }

    return render(request, 'djmessenger/chat.html', data)


def user_chat(request, userid):
    user = request.user
    friend = CustomUser.objects.get(id=userid)
    friends = user.contact.all()
    message_list = Message.objects.all()

    # Search
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        user_list = CustomUser.objects.filter(search)
    else:
        user_list = CustomUser.objects.all()

    # Send message
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = friend
            chat_message.save()
    form = MessageForm

    data = {
        'message_form': form,
        'message_list': message_list,
        'userid': userid,
        'user': user,
        'friend': friend,
        'friends': friends,
        'user_list': user_list,
    }
    return render(request, 'djmessenger/user_chat.html', data)
