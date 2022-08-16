from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DeleteView, UpdateView, CreateView, TemplateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.forms import PostForm, CommentForm
from blog.models import Post, Comments, Category
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, "blog/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/signup.html"


class PostListView(ListView):
    model = Post
    paginate_by = 100
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['comment_form'] = CommentForm()
        context['comments'] = Comments.objects.filter(post_id=kwargs['object'].pk)
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('post-list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_delete.html'


# class Index(TemplateView):
#     template_name = "post_list.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['categories'] = Category.objects.all()
#         return context

class CategoryList(ListView):
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.all().select_related('category')

# def post_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         posts = posts.filter(category=category)
#     return render(request, 'blog/list.html', {'category': category, 'categories': categories, 'posts': posts})


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.reqest, self.success_msg)
        return super().form_valid(form)

    def get_seccess_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


# class LoginView(FormMixin, DetailView):
#     model = User
#     # form_class = LoginForm
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_anonymous:
#             return render(request, 'blog/templates/registration/login.html', context={
#                 'form': self.form_class(),
#                 'error': kwargs.get('error')
#             })
#         return HttpResponseRedirect('/')

    # def post(self, request, *args, **kwargs):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         login(request, user)
    #         return HttpResponseRedirect('/')
    #
    #     return self.get(request, error="invalid username or password")


class PostCommentView(FormMixin, DetailView):
    model = Comments
    form_class = CommentForm

    def get_success_url(self):
        return "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        self.object = form.save(commit=False)
        self.object.post = Post.objects.get(pk=kwargs['pk'])
        self.object.author = request.user
        self.object.save()
        if form.is_valid():
            return redirect('post-detail', pk=kwargs['pk'])
