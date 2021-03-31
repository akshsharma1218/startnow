from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView,
    CreateView
)
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'Blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self,**kwargs):
        post = self.get_object()
        request = self.request
        is_liked=False
        if post.likes.filter(id=request.user.id).exists():
            is_liked=True
        context = super().get_context_data(**kwargs)
        context.update({'total_likes': post.total_likes(), 'is_liked': is_liked})
        context ['comments'] = Comment.objects.filter(post=post)
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model         = Comment
    template_name ='Blog/comment_create.html'
    fields        = ['cont']


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SearchResultView(ListView):
    model = Post
    template_name='Blog/search_result.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
        Q(title__icontains=query) | Q(author__username=query))
        if query == '19 May,2001':
            object_list = ['19 May,2001']
        return object_list



def like_post(request):
    post = get_object_or_404(Post,id=request.POST.get('id'))
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:
        post.likes.add(request.user)
        is_liked=True
    context={
            'post':post,
            'is_liked':is_liked,
            'total_likes':post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('Blog/like_sections.html', context, request = request)
        return JsonResponse({ 'form': html })


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
