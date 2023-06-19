from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
from django.db.models import Q
from account.models import CustomUser
from django.http import JsonResponse
from account.forms import CustomUserChangeForm
import json
# Create your views here.


def home_view(request):
    return render(request, 'djmessenger/homepage.html')


def profile_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        user_list = CustomUser.objects.filter(search)
    else:
        user_list = CustomUser.objects.all()

    # Edit_profile

    if request.method == 'POST':
        user_upd_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if user_upd_form.is_valid():
            user_upd_form.save()
            return redirect('profile')
    else:
        user_upd_form = CustomUserChangeForm(instance=request.user)

    data = {
        'user_list': user_list,
        'user_upd_form': user_upd_form
    }
    return render(request, 'djmessenger/profile.html', data)


def chat_view(request):
    user = request.user
    friends = user.contacts.all
    print(friends)
    # Search
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        user_list = CustomUser.objects.filter(search)
    else:
        user_list = CustomUser.objects.all()

    data = {
        'user_list': user_list,
        'friends': friends,
        'user': user,
    }
    return render(request, 'djmessenger/chat.html', data)


def user_chat(request, userid):
    user = request.user
    friend = CustomUser.objects.get(id=userid)
    friends = user.contacts.all()
    print(friends)
    message_list = Message.objects.order_by('date')
    rec_message_list = Message.objects.filter(msg_sender=friend, msg_receiver=user)

    # Search
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        user_list = CustomUser.objects.filter(search)
    else:
        user_list = CustomUser.objects.all()

    # Send_message
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
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
        'num': rec_message_list.count(),
    }
    return render(request, 'djmessenger/user_chat.html', data)


# Async
def sent_messages(request, userid):
    user = request.user
    friend = CustomUser.objects.get(id=userid)
    data = json.loads(request.body)
    new_chat = data['msg']
    new_chat_message = Message.objects.create(message=new_chat, msg_sender=user, msg_receiver=friend)
    return JsonResponse(new_chat_message.body, safe=False)


def received_messages(request, userid):
    user = request.user
    friend = CustomUser.objects.get(id=userid)
    arr = []
    message_list = Message.objects.filter(msg_sender=friend, msg_receiver=user)
    for m in message_list:
        arr.append(m.message)
    return JsonResponse(arr, safe=False)
