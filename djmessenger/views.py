from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message, UserList
from django.db.models import Q
from account.models import CustomUser, BlockedUser, ContactList
from django.http import JsonResponse
from account.forms import CustomUserChangeForm
import json
# Create your views here.


# Profile_Page
def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('signup')

    user = request.user
    friends = ContactList.objects.filter(user=user)
    blocked_list = BlockedUser.objects.filter(user=user)

    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        search_list = CustomUser.objects.filter(search)
        user_list = None
    else:
        search_list = None
        user_list = UserList.objects.filter(user=user)

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
        'user_upd_form': user_upd_form,
        'friends': friends,
        'blocked_list': blocked_list,
        'search_list': search_list,
    }
    return render(request, 'djmessenger/profile.html', data)


# Home
def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('signup')

    user = request.user
    friends = ContactList.objects.filter(user=user)

    # Search
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        search_list = CustomUser.objects.filter(search)
        user_list = None
    else:
        search_list = None
        user_list = UserList.objects.filter(user=user)

    data = {
        'user_list': user_list,
        'friends': friends,
        'user': user,
        'search_list': search_list,
    }
    return render(request, 'djmessenger/chat.html', data)


# User_Chat_Page
def user_chat(request, userid):
    if not request.user.is_authenticated:
        return redirect('signup')

    user = request.user
    friend = CustomUser.objects.get(id=userid)
    friends = ContactList.objects.filter(user=user)
    message_list = Message.objects.order_by('date')
    lm = Message.objects.all()
    try:
        add_friend = ContactList.objects.get(friend=userid, user=user)
    except:
        add_friend = None

    try:
        blocked_friend = BlockedUser.objects.get(friend=userid, user=user)
    except:
        blocked_friend = None
    try:
        blocked_user = BlockedUser.objects.get(friend=user, user=userid)
    except:
        blocked_user = None

    blocked_list = BlockedUser.objects.all()

    rec_message_list = Message.objects.filter(msg_sender=friend, msg_receiver=user)

    # Search
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        search_list = CustomUser.objects.filter(search)
        user_list = None
    else:
        search_list = None
        user_list = UserList.objects.filter(user=user)

    # Send_message
    if request.method == 'POST':
        new_chat = UserList()
        receiver_chat = UserList()
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid:
            if UserList.objects.filter(user=user, receiver_user=friend):
                chat_message = form.save(commit=False)
                chat_message.msg_sender = user
                chat_message.msg_receiver = friend
                chat_message.save()
            else:
                new_chat.user = user
                new_chat.receiver_user = friend
                new_chat.save()

                receiver_chat.user = friend
                receiver_chat.receiver_user = user
                receiver_chat.save()

                chat_message = form.save(commit=False)
                chat_message.msg_sender = user
                chat_message.msg_receiver = friend
                chat_message.save()

        return redirect('user_chat', userid)
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
        'blocked_list': blocked_list,
        'blocked_friend': blocked_friend,
        'blocked_user': blocked_user,
        'add_friend': add_friend,
        'search_list': search_list,
        'lm': lm,
    }
    return render(request, 'djmessenger/user_chat.html', data)


# Add_Friend_Func
def add_new_friend(request, operation, pk):
    new_friend = CustomUser.objects.get(pk=pk)
    if operation == 'add':
        contact_list = ContactList(user=request.user, friend=new_friend)
        contact_list.save()
    if operation == 'remove':
        ContactList.objects.filter(user=request.user, friend=new_friend).delete()
    back = request.META.get('HTTP_REFERER')
    return redirect(back, pk)


# Block_User_Func
def block_user(request, operation, pk):
    block_users = CustomUser.objects.get(pk=pk)
    if operation == 'block':
        block__user = BlockedUser(user=request.user, friend=block_users)
        block__user.save()
    elif operation == 'unblock':
        BlockedUser.objects.filter(user=request.user, friend=block_users).delete()
    back = request.META.get('HTTP_REFERER')
    return redirect(back, pk)


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
