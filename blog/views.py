from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_comm = form.save()
            new_comm.slug = slugify(new_comm.title)
            new_comm.save()

        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content',)
    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_comm = form.save()
            new_comm.slug = slugify(new_comm.title)
            new_comm.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

class BlogListView(ListView):
    model = Blog

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(publication=True)
    #     return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

def toggle_activity(request, pk):
    comm_item = get_object_or_404(Blog, pk=pk)
    if comm_item.publication:
        comm_item.publication = False
    else:
        comm_item.publication = True

    comm_item.save()

    return redirect(reverse('blog:list'))