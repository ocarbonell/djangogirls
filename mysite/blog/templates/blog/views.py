from django.shortcuts import render, get_object_or_404


def post_detail(request, pk):
    from mysite.blog.models import Post
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html', {'post':post})