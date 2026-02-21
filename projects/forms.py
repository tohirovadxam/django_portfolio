from django import forms
from .models import Projects, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'language', 'description', 'image', 'document', 'github_url', 'live_url', 'status']

        # Inputlarga Tailwind styllarini beramiz
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white'}),
            'language': forms.Select(
                attrs={'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white'}),
            'description': forms.Textarea(
                attrs={'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white', 'rows': 5}),
            'status': forms.Select(
                attrs={'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white'}),
            'github_url': forms.URLInput(
                attrs={'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white'}),
            'live_url': forms.URLInput(
                attrs={'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'w-full bg-slate-800 border border-slate-700 rounded-xl p-4 text-white focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all placeholder-slate-500',
                'rows': 3,
                'placeholder': 'Loyiha haqida fikringiz...'
            }),
        }