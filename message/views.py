from django.shortcuts import render
from message.models import Message
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.forms import formset_factory


@login_required
def user_inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'message/inbox.html', {'messages': messages})


@login_required
def user_outbox(request):
    MessageFormSet = formset_factory(MessageForm)
    if request.method == 'POST':
        formset = MessageForm(request.POST, request.FILES)

        if formset.is_valid():
            formset.save()

    else:
        formset = MessageFormSet()

    return render(request, 'message/outbox.html', {'formset': formset})
