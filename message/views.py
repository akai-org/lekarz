from django.shortcuts import render
from message.models import Message
from django.contrib.auth.decorators import login_required


@login_required
def user_inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'message/inbox.html', {'messages': messages})
