from django.shortcuts import render
from django.views.generic import ListView
from .models import Notificacao


def listar_notific(request):
    not_all = Notificacao.objects.all().filter(sender=request.user).exclude(owner=request.user)
    return render(request, 'notificacao/not_list.html',
                    {'not_all': not_all,})


"""class NotificationListView(ListView):
    template_name = 'notifications/not_list.html'
    context_object_name = 'not_all'

    def get_queryset(self):
        return Notificacao.objects.all().exclude(user=self.request.user)"""
