from django.shortcuts import render

from .models import Aluno, Curso, Professor

def cursos_view(request):
    cursos = (
        Curso.objects
        .select_related('professor')
        .prefetch_related('alunos')
        .all()
    )

    cursos_com_imagem = []
    for curso in cursos:
        imagem = next(
            (aluno.fotografia for aluno in curso.alunos.all() if aluno.fotografia),
            None,
        )
        cursos_com_imagem.append({'curso': curso, 'imagem': imagem})

    return render(
        request,
        'escola/cursos.html',
        {'cursos_com_imagem': cursos_com_imagem},
    )


def professores_view(request):
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(
        request,
        'escola/professores.html',
        {'professores': professores},
    )


def alunos_view(request):
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(
        request,
        'escola/alunos.html',
        {'alunos': alunos},
    )
