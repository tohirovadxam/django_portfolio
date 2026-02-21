from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, CommentForm
from .models import Projects, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def project_list(request):
    projects = Projects.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def project_detail(request, slug):
    project = get_object_or_404(Projects, slug=slug)

    comments = project.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.author = request.user
            comment.save()
            return redirect('projects:project_detail', slug=project.slug)
    else:
        form = CommentForm()

    context = {'project': project, 'comments': comments, 'form': form}
    return render(request, 'projects/project_detail.html', context)


def project_create(request):

    if not request.user.is_superuser:
        raise Http404()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects:project_list')
    else:
        form = ProjectForm()

    return render(request, 'projects/project_create.html', {'form': form})


def project_update(request, slug):

    if not request.user.is_superuser:
        raise Http404()

    project = get_object_or_404(Projects, slug=slug)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:project_detail', slug=project.slug)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_create.html', {'form': form})

def project_delete(request, slug):

    if not request.user.is_superuser:
        raise Http404()

    project = get_object_or_404(Projects, slug=slug)

    if request.method == 'POST':
        project.delete()
        return redirect('projects:project_list')

    return render(request, 'projects/confirm_delete.html', {'project': project})


@login_required
def delete_comment(request, pk):
    # Izohni ID bo'yicha topamiz
    comment = get_object_or_404(Comment, pk=pk)

    # Qayta yo'naltirish uchun loyiha slug'ini saqlab olamiz
    project_slug = comment.project.slug

    # XAVFSIZLIK TEKSHIRUVI:
    # O'chirayotgan odam izoh muallifi YOKI Superuser bo'lishi shart
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
        messages.success(request, "Izoh muvaffaqiyatli o'chirildi.")
    else:
        messages.error(request, "Siz bu izohni o'chira olmaysiz!")

    # O'sha loyiha sahifasiga qaytamiz
    return redirect('projects:project_detail', slug=project_slug)
