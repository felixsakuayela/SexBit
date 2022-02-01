from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Perfil, User
from .forms import PerfilForm
from postes.models import Poste
from postes.forms import PosteForm
from comentarios.models import Comment
from comentarios.forms import CommentForm

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def index(request):

    allposte = Poste.objects.all()
    teste1 = Poste.objects.all()
    allcomentario = Comment.objects.all()


    return render(request, 'index.html',
                      {'allposte': allposte, 'allcomentario': allcomentario,  'teste1': teste1, })

    """num_video = Video.objects.all().count()
    pub = Video.objects.all().order_by('-v_created_at')[:num_video]"""


@login_required
def portal(request):
    User = get_user_model()
    usuarios = User.objects.all()
    dados = Perfil.objects.filter(Usuario=request.user)
    return render(request, 'usuarios/perfil.html',
                  {'User': User, 'usuarios': usuarios, 'dados': dados})

@login_required
def salavip(request):
    usuario_atual = request.user

    if usuario_atual is True:
        User = get_user_model()
        usuarios = User.objects.all()
        nome = Perfil.Nome_Completo
        dados = Perfil.objects.filter(Usuário=request.user)
        return render(request, 'usuarios/sala-vip.html',
                      {'User': User, 'usuarios': usuarios, 'dados': dados, 'nome': nome})
    else:
        return render(request, 'usuarios/sala-vip.html')


def perfil(request, id):

    User = get_user_model()
    usuarios = User.objects.all()
    perfil = get_object_or_404(User, pk=id)

    nome = perfil.username


    return render(request, 'usuarios/perfil.html',
                  {'User': User, 'usuarios': usuarios, 'nome': nome, 'perfil': perfil,})

@login_required
def sala(request, id):

    user_obj = get_object_or_404(User, pk=id)
    nome = user_obj.username
    session_user = get_object_or_404(User, username=request.user)
    user_following = session_user
    session_following, create = Perfil.objects.get_or_create(Usuario=session_user)
    following, create = Perfil.objects.get_or_create(Usuario=session_user.id)
    check_user_followers = Perfil.objects.filter(followers=user_obj).count()


    if Perfil.objects.filter(Usuario=user_obj.id).exists():
        p4 = Perfil.objects.get(Usuario=user_obj.id)
        user_following = p4.followers.all().count()
    else:
        user_following = 0

    is_followed = False
    if session_following.followers.filter(pk=id).exists() or following.followers.filter(pk=id).exists():
        is_followed=True
    else:
        is_followed = False
    param1 = {'User': User, 'nome': nome, 'user_obj': user_obj, 'followers': check_user_followers, 'user_following': user_following, 'is_followed': is_followed}

    param2 = {'user_obj': user_obj, 'user_following': user_following, 'followers': check_user_followers,
              'following': following, 'is_followed': is_followed}
    if 'Usuario' in request.session:
        return render(request, 'usuarios/sala.html', param1, param2)
    else:
        return render(request, 'usuarios/sala.html', param1)



@login_required
def follow_user(request, id):
    other_user = get_object_or_404(User, pk=id)
    session_user = request.user
    get_user = get_object_or_404(User, username=session_user)
    check_follower = Perfil.objects.get(Usuario=session_user.id)

    is_followed = False
    if other_user.username != session_user:
        if check_follower.followers.filter(username=other_user).exists():
            add_usr = Perfil.objects.get(Usuario=get_user.id)
            add_usr.followers.remove(other_user)
            is_followed = False
            return redirect(f'/sala/{other_user.id}')
        else:
            add_usr = Perfil.objects.get(Usuario=get_user)
            add_usr.followers.add(other_user)
            is_followed = True
            return redirect(f'/sala/{other_user.id}')

        return redirect(f'/sala/{other_user.id}')
    else:
        return redirect(f'/sala/{other_use.id}')

@login_required
def novoperfil(request):
    usuario_atual = request.user
    if request.method == 'POST':
        form = PerfilForm(request.POST)

        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.Usuario = request.user
            perfil.save()
            return redirect('perfil', usuario_atual.id)
    else:
        form = PerfilForm()
        return render(request, 'usuarios/novoperfil.html', {'form': form})

@login_required
def editarperfil(request):

    current_user = request.user

    if request.method == 'POST':
        if Perfil.objects.filter(Usuario_id=current_user).exists():
            form = PerfilForm(request.POST, instance=Perfil.objects.get(Usuario_id=current_user))
        else:
            form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.Usuario = current_user
            perfil.save()
            return redirect('perfil', current_user.id)
    else:
        if Perfil.objects.filter(Usuario_id=current_user).exists():
            form = PerfilForm(instance=Perfil.objects.get(Usuario_id=current_user))
        else:
            form = PerfilForm()

    return render(request, 'usuarios/editarperfil.html', {"form": form})