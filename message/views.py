from django.shortcuts import render, redirect
from message.models import Message


def user_inbox(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'message/inbox.html', {'messages': messages})
