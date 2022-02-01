from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Comment
from postes.models import Poste
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt




def listar_poste(request):

    return render(request, 'index.html',)