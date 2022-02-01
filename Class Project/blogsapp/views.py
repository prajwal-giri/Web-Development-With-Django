from email import header
from django.shortcuts import render
from .models import Cblogs
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BlogForm
from django.urls import reverse_lazy


def fblog(request):
    context = {
        "result": Cblogs.objects.all()
    }
    return render(request, "blogfolder/blog.html", context)


def detail(request, blog_id):
    context = {
        'dresult': Cblogs.objects.get(id=blog_id)
    }
    return render(request, 'blogfolder/blogdetail.html', context)


# class BlogCreateView(CreateView):
#     model = Cblogs
#     template_name = 'blogfolder/blog_create.html'
#     fields = ['title', 'author', 'body','text','developer']


class BlogCreateView(CreateView):  # new
    model = Cblogs
    form_class = BlogForm
    template_name = 'blogfolder/blog_create.html'
    # fields = ['title','subtitle', 'author', 'body']  #or fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Cblogs
    #form_class = BlogForm
    template_name = 'blogfolder/blog_edit.html'
    fields = ['title', 'body', 'text', 'developer', 'header_image']


class BlogDeleteView(DeleteView):
    model = Cblogs
    template_name = 'blogfolder/blog_delete.html'
    success_url = reverse_lazy('blog1')
