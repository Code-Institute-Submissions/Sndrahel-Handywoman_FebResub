from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm, BlogForm


# code below adapted from Code Institute blog tutorial
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


class PostDetail(View):

    def get(self, request, blog_id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = Post.objects.get(id=blog_id)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, blog_id, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = Post.objects.get(id=blog_id)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )

# Code below adapted from:
# https://github.com/jjpickering10/CI-MS4-DragonEggWoodturning/blob/main/blog/views.py


@login_required
def add_post(request):

    if not request.user.is_superuser:
        messages.info(request, 'Only admin can do that')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            new_post = blog_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'New post added')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Error posting to blog')
            return redirect(reverse('blog'))
    else:
        blog_form = BlogForm()

    template = 'add_post.html'

    context = {
        'blog_form': blog_form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, blog_id):

    if not Post.objects.filter(id=blog_id).exists():
        messages.info(request, 'Doesnt exist')
        return redirect(reverse('blog'))

    if not request.user.is_superuser:
        messages.info(request, 'Only admin can do that')
        return redirect(reverse('blog'))

    post = Post.objects.get(id=blog_id)

    if request.method == 'POST':
        edited_post = BlogForm(request.POST, request.FILES, instance=post)
        if edited_post.is_valid():
            edited_post.save()
            messages.success(request, f'Blog post {post.title} edited')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, f'Error editing post {post.title}')
            return redirect(reverse('post_detail', args=[post.id]))
    else:
        blog_form = BlogForm(instance=post)

    template = 'edit_post.html'

    context = {
        'post': post,
        'blog_form': blog_form
    }

    return render(request, template, context)


@login_required
def delete_post(request, blog_id):

    if not Post.objects.filter(id=blog_id).exists():
        messages.info(request, 'Doesnt exist')
        return redirect(reverse('blog'))

    if not request.user.is_superuser:
        messages.info(request, 'Only admin can do that')
        return redirect(reverse('blog'))

    post = Post.objects.get(id=blog_id)
    post.delete()
    messages.success(request, f'Blog post {post.title} deleted')

    return redirect(reverse('blog'))


def like_post(request, blog_id):

    if not Post.objects.filter(id=blog_id).exists():
        messages.info(request, 'Doesnt exist')
        return redirect(reverse('blog'))

    if not request.user.is_authenticated:
        messages.info(request, 'Only registered users can like a post')
        return redirect(reverse('post_detail', args=[blog_id]))

    post = Post.objects.get(id=blog_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post.like_count -= 1
        post.save()
        messages.success(request, f'You unliked {post.title}')
    else:
        post.likes.add(request.user)
        post.like_count += 1
        post.save()
        messages.success(request, f'You liked {post.title}')

    return redirect(reverse('post_detail', args=[blog_id]))
