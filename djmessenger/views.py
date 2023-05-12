from django.shortcuts import render
from .forms import MessageForm
from .models import Message
from django.db.models import Q

from account.models import CustomUser
# Create your views here.


def home_view(request):
    return render(request, 'djmessenger/homepage.html')


def chat_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(username__icontains=q))
        contacts_list = CustomUser.objects.filter(search)
    else:
        contacts_list = CustomUser.objects.all()

    message_list = Message.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            form.save()
    form = MessageForm

    data = {
        "message_form": form,
        "message_list": message_list,
        "contacts_list": contacts_list,
    }
    return render(request, 'djmessenger/chat.html', data)
