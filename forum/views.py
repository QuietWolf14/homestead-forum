from django.shortcuts import render, get_object_or_404, redirect
from .models import ForumGroup, Forum, Post, Comment
from accounts.models import UserProfile
from .forms import PostForm, CommentForm

def forum_home_view(request):
    context = {}
    forum_groups = ForumGroup.objects.all()
    forums = Forum.objects.all()

    context['forum_groups'] = forum_groups
    context['forums'] = forums
    return render(request, 'forum/home.html', context)


def forum_view(request, forum_id):
    context = {}
    forum = get_object_or_404(Forum, pk=forum_id)
    forum_posts = Post.objects.filter(forum__id=forum_id)

    context['forum'] = forum
    context['forum_posts'] = forum_posts
    context['post_count'] = forum_posts.count()

    return render(request, 'forum/forum.html', context)


def post_view(request, post_id):
    context = {}
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post__id=post_id)
    context['post'] = post
    context['comments'] = comments
    context['comment_count'] = comments.count()

    return render(request, 'forum/post.html', context)


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.forum = get_object_or_404(Forum, pk=request.POST.get('forum_id'))
            post.title = form.cleaned_data["title"]
            post.author = request.user
            post.text = form.cleaned_data["text"]
            post.save()
            return redirect('forum:post', post_id=post.pk)

    else:
        context = {}
        context['form'] = PostForm()
        forum = get_object_or_404(Forum, pk=request.GET['forum_id'])
        context['forum'] = forum

        return render(request, 'forum/edit_post.html', context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.title = form.cleaned_data["title"]
            post.text = form.cleaned_data["text"]
            post.save()
            return redirect('forum:post', post_id=post.pk)

    else:
        context = {}
        context['form'] = PostForm(instance=post)
        context['forum'] = get_object_or_404(Forum, pk=post.forum.id)

    return render(request, 'forum/edit_post.html', context)


def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=request.POST.get('post_id'))
            comment.text = form.cleaned_data["text"]
            comment.author = request.user
            comment.save()
            return redirect('forum:post', post_id=comment.post.id)

    else:
        context = {}
        context['form'] = CommentForm()
        post = get_object_or_404(Post, pk=request.GET['post_id'])
        context['post'] = post

        return render(request, 'forum/edit_comment.html', context)


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        form = CommentFormForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.text = form.cleaned_data["text"]
            comment.save()
            return redirect('forum:post', post_id=comment.post.id)

    else:
        context = {}
        context['form'] = CommentForm(instance=comment)
        context['forum'] = get_object_or_404(Forum, pk=post.forum.id)

    return render(request, 'forum/edit_comment.html', context)


def user_profile_view(request, username):
    context = {}
    context['profile'] = get_object_or_404(UserProfile, user_id=request.user.id)

    return render(request, 'forum/user_profile.html', context)
