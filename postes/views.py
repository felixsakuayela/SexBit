from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import Poste, User
from .forms import PosteForm
from notificacao.models import Notificacao
from comentarios.models import Comment
from comentarios.models import Comment2
from comentarios.forms import CommentForm
from comentarios.forms import CommentForm2
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@login_required
def poste(request, id):

    User = get_user_model()
    usuarios = User.objects.all()
    perfil = get_object_or_404(User, pk=id)
    nome = perfil.username
    formposte = PosteForm()

    if (request.method == 'POST'):
        formposte = PosteForm(request.POST, request.FILES)

        if formposte.is_valid():
            poste = formposte.save(commit=False)
            poste.User_Poste = request.user
            poste.save()

            return redirect('postar_retorno', request.user.id)
        else:
            return render(request, 'postes/poste.html',
                          {'formposte': formposte, })

    else:

        return render(request, 'postes/poste.html',
                      {'formposte': formposte, })


def ver_poste(request, id):
    poste = get_object_or_404(Poste, pk=id)

    session_user = get_object_or_404(User, username=request.user)
    num_reac_forc = poste.p_braco_forca.all().count()
    num_reac_corac = poste.p_cara_coracao.all().count()

    allcomentario = Comment.objects.filter(poste_id=poste)
    allposte = Poste.objects.all()
    f = poste

    is_reac_forc = False
    if poste.p_braco_forca.filter(pk = session_user.id).exists():
        is_reac_forc = True
    else:
        is_reac_forc = False

    is_reac_corac = False
    if poste.p_cara_coracao.filter(pk = session_user.id).exists():
        is_reac_corac = True
    else:
        is_reac_corac = False


    formcomentario = CommentForm()
    if (request.method == 'POST'):
        formcomentario = CommentForm(request.POST, request.FILES)
        if formcomentario.is_valid():

            comenta = formcomentario.save(commit=False)
            comenta.poste_id = Poste.objects.get(Texto = poste.Texto, User_Poste = poste.User_Poste, Foto = poste.Foto, Video = poste.Video, v_created_at = poste.v_created_at, v_updated_at = poste.v_updated_at, )
            comenta.commenter = request.user
            comenta.save()
            notification_type = ContentType.objects.get(app_label='comentarios', model='comment')
            notif = Notificacao.objects.create(notification_type=notification_type,
                                               notification_id=comenta.comment_id,
                                               link_name='vercomentario',
                                               owner=request.user,
                                               sender=poste.User_Poste,
                                               notificacao_alert=10)
            notif.save()

            return redirect('verposte', poste.poste_id)
        else:
            return render(request, 'postes/ver_poste.html',
                          {
                            'num_reac_forc': num_reac_forc, 'is_reac_forc': is_reac_forc,
                            'num_reac_corac': num_reac_corac, 'is_reac_corac': is_reac_corac,
                           'poste': poste,  'allcomentario': allcomentario, 'formcomentario': formcomentario,
                          })

    else:

        return render(request, 'postes/ver_poste.html',
                      {
                        'num_reac_forc': num_reac_forc, 'is_reac_forc': is_reac_forc,
                          'num_reac_corac': num_reac_corac, 'is_reac_corac': is_reac_corac,
                          'poste': poste, 'allcomentario': allcomentario, 'formcomentario': formcomentario
                      })



@login_required
def reac_forca(request, id):
    other_user = get_object_or_404(Poste, pk=id)
    get_user = get_object_or_404(User, username=request.user)

    is_reac_forc = False
    if other_user.p_braco_forca.filter(pk = get_user.id).exists():
        add_usr = Poste.objects.get(poste_id=other_user.poste_id)
        add_usr.p_braco_forca.remove(get_user)
        is_reac_forc = False
        return redirect(f'/ver_poste/{other_user.poste_id}')
    else:
        add_usr = Poste.objects.get(poste_id=other_user.poste_id)
        add_usr.p_braco_forca.add(get_user)

        add_usr = Poste.objects.get(poste_id=other_user.poste_id)
        add_usr.p_cara_coracao.remove(get_user)
        is_reac_forc = True
        is_reac_corac = False
        return redirect(f'/ver_poste/{other_user.poste_id}')

    return redirect(f'/ver_poste/{other_user.poste_id}')


@login_required
def reac_corac(request, id):
    other_user = get_object_or_404(Poste, pk=id)
    get_user = get_object_or_404(User, username=request.user)

    is_reac_corac = False
    if other_user.p_cara_coracao.filter(pk = get_user.id).exists():
        add_usr = Poste.objects.get(poste_id=other_user.poste_id)
        add_usr.p_cara_coracao.remove(get_user)
        is_reac_corac = False
        return redirect(f'/ver_poste/{other_user.poste_id}')
    else:
        add_usr = Poste.objects.get(poste_id=other_user.poste_id)
        add_usr.p_cara_coracao.add(get_user)

        add_usr2 = Poste.objects.get(poste_id=other_user.poste_id)
        add_usr2.p_braco_forca.remove(get_user)
        is_reac_forc = False
        is_reac_corac = True
        return redirect(f'/ver_poste/{other_user.poste_id}')

    return redirect(f'/ver_poste/{other_user.poste_id}')


def ver_comentario(request, id):
    comentario2 = get_object_or_404(Comment, pk=id)
    allcomentario = Comment2.objects.filter(comment_id=comentario2)


    formcomentario2 = CommentForm2()

    if (request.method == 'POST'):
        formcomentario2 = CommentForm2(request.POST, request.FILES)
        if formcomentario2.is_valid():

            comenta2 = formcomentario2.save(commit=False)
            comenta2.comment_id = Comment.objects.get(C_Texto = comentario2.C_Texto, commenter = comentario2.commenter, C_Foto = comentario2.C_Foto, C_Video = comentario2.C_Video, c_created_at = comentario2.c_created_at, c_updated_at = comentario2.c_updated_at,  active = comentario2.active,  reply = comentario2.reply, )
            comenta2.commenter2 = request.user

            comenta2.save()

            return redirect('vercomentario', comentario2.comment_id)
        else:
            return render(request, 'postes/ver_poste.html',
                          {'comentario2': comentario2,   'allcomentario': allcomentario, 'formcomentario2': formcomentario2, })

    else:
        return render(request, 'postes/ver_comentario.html',
                      {'comentario2': comentario2, 'allcomentario': allcomentario, 'formcomentario2': formcomentario2, })



def listar_poste(request):

    return render(request, 'postes/lposte.html')

