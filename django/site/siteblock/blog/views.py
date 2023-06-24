from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post, Category, Tag
from django.db.models import F

class home(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "class"
        return context
    


class PostBYCategry(ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["slug"])
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(slug=self.kwargs["slug"])
        return context



class GetPost(DeleteView):
    model = Post
    template_name = "blog/single.html"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

