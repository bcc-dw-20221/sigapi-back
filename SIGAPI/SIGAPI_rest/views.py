from django.shortcuts import render, HttpResponse
from SIGAPI_rest.models import Curso
from django.core import serializers
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_Cursos(request):
    aluno = Curso.objects.all()
    resp_json = serializers.serialize("json", aluno)
    return HttpResponse (resp_json, content_type="application/json")
@require_http_methods(["POST"])
def post_Curso(request):
    nova = Curso()
    nova.nome = request.POST("nome")
    nova.data_vigor = request.POST("data_vigor")
    nova.matriz_curricular = request.POST("matriz.curricular")
    nova.save()
    return HttpResponse("curso salvo com sucesso")
@require_http_methods(["DELETE"])
def delete_Curso(request, curso_id):
    post = Curso.objects.get(pk=curso_id)
    post.delete()
    return HttpResponse("Deletado com sucesso.")
@require_http_methods(["GET"])
def get_Curso(request, curso_id):
    """Retorna aluno especifico."""
    cursox = Curso.objects.filter(pk=curso_id)
    aluno_json = serializers.serialize("json", cursox)
    return HttpResponse(aluno_json , content_type="application/json")

@require_http_methods(["GET"])
def get_user(request, user_id):
    user = get_user_model(pk=user_id)
    user_json = serializers.serialize("json", user)
    return HttpResponse(user_json, content_type="application/json")
    