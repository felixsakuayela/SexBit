from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Mensagem
from .forms import MensagemForm
from django.shortcuts import get_object_or_404

@login_required
def mensagem(request, id):
    User = get_user_model()
    usuarios = User.objects.all()

    Userid1 = get_object_or_404(User, username=request.user)
    nome1 = Userid1.username

    Userid2 = get_object_or_404(User, pk=id)
    nome2 = Userid2.username

    dados = User.objects.filter(pk=id)

    mensaum = Mensagem.objects.filter(user=Userid1, rec_user=Userid2)
    mensis = Mensagem.objects.filter(user=Userid2, rec_user=Userid1)

    mensagens = mensaum | mensis

    if request.method == 'POST':
        form = MensagemForm(request.POST)

        if form.is_valid():
            caixa = form.save(commit=False)

            caixa.user = Userid1

            caixa.rec_user = Userid2

            caixa.save()

            return redirect('mensagem', Userid2.id)
        else:
            return render(request, 'mensagens/mensagem.html',
                          {'Userid1': Userid1, 'User': User, 'usuarios': usuarios, 'dados': dados,
                           'mensagens': mensagens, 'nome2': nome2, 'nome1': nome1, 'form': form})

    else:
        form = MensagemForm()
        return render(request, 'mensagens/mensagem.html',
                      {'Userid1': Userid1, 'User': User, 'usuarios': usuarios, 'dados': dados,
                       'mensagens': mensagens, 'nome2': nome2, 'nome1': nome1, 'form': form})


@login_required
def mensagem2(request, id):
    User = get_user_model()
    usuarios = User.objects.all()
    Userid = get_object_or_404(User, pk=id)
    perfis  = Perfil.objects.all()
    perfil = get_object_or_404(perfis, pk=id)
    dados = Perfil.objects.filter(pk=id)
    mensaum = Message.objects.filter(user=request.user, rec_user=perfil.Usuário)
    mensis = Message.objects.filter(user=perfil.Usuário, rec_user=request.user)


    aperfil = get_object_or_404(Perfil, pk=id)
    nome2 = aperfil.Nome_Completo

    aperfil = get_object_or_404(Perfil, Usuário=request.user)
    nome1 = aperfil.Nome_Completo

    mensagens = mensaum | mensis


    if request.method == 'POST':
        form = MensagemForm(request.POST)

        if form.is_valid():
            caixa = form.save(commit=False)

            caixa.user = request.user

            caixa.rec_user = perfil.Usuário

            caixa.save()

            return redirect('mensagem', perfil.Usuário.id)
        else:
            return render(request, 'mensagens/mensagem.html',
                    {'Userid': Userid, 'perfil': perfil, 'perfis': perfis, 'User': User, 'usuarios': usuarios, 'dados': dados,
                    'mensagens': mensagens, 'nome2': nome2, 'nome1': nome1, 'form': form})

    else:
        form = MensagemForm()
        return render(request, 'mensagens/mensagem.html',
                  {'Userid': Userid, 'perfil': perfil, 'perfis': perfis, 'User': User, 'usuarios': usuarios, 'dados': dados,
                   'mensagens': mensagens,  'nome2': nome2, 'nome1': nome1, 'form': form})

