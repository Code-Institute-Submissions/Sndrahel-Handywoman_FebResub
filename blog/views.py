from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
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
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
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
                "liked": liked
            },
        )

class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Add a new blog post to Blog page
# Help from Master Code Online
@login_required
def add_post(request):
    """ Add a new blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    form = CommentForm(request.POST or None)
    template = 'add_post.html'

    try:
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Yahoo! A new blog post has been uploaded \
                             to the database')

            return redirect(reverse('blog', args=[post.id]))

    except Exception as e:
        form = CommentForm()
        messages.warning(request,
                         'Blog post was not saved. Error: {}'.format(e))

    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit a blog post on Blog page
# Help from Master Code Online
@login_required
def edit_post(request, pk):
    """ Edit an existing blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'You have successfully edited this post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request,
                           'Error: Blog post was not saved.')
    else:
        form = CommentForm(instance=post)

    template = 'edit_post.html'
    context = {
        'form': form,
        'post': post,
        }

    return render(request, template, context)


# Delete a post from the blog page
@login_required
def delete_post(request, pk):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
