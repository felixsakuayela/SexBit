from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Foto
from .forms import FotoForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

@login_required
def Post_foto(request, id):

    aperfil = get_object_or_404(Perfil, pk=id)
    nome = aperfil.Nome_Completo

    formfoto = FotoForm()

    if (request.method == 'POST'):
        formfoto = FotoForm(request.POST, request.FILES)

        if (formfoto.is_valid()):
            foto = formfoto.save(commit=False)
            foto.User_foto = request.user
            foto.Nome_foto = nome
            foto.save()

            return redirect('perfil', request.user.id)
        else:
            return render(request, 'usuarios/foto.html',
                          {'formfoto': formfoto, })

    else:

        return render(request, 'usuarios/foto.html',
                      {'formfoto': formfoto, })
