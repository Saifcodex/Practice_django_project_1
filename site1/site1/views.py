from django.shortcuts import render
from posts.models import Post
from products.models import Product


def home(request):
    return render(request, 'Home.html')


def post(request):
    post = Post.objects.all()
    return render(request, 'PostPage.html', {
        "post": post
    })


def product(request):
    product = Product.objects.all()
    return render(request, 'ProductPage.html', {
        "product": product
    })
