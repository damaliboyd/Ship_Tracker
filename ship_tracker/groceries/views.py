from django.shortcuts import render
from .models import Grocery
# Create your views here.



def post_new(request):
    if request.method == "POST":
        form = GorceryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('grocery_detail', pk=post.pk)
    else:
        form = GorceryForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
def grocery_list(request):
    post = Grocery.objects.all()
    return render(request, 'grocery/grocery_list.html', {'posts': posts})

def grocery_detail(request, pk):
    post = get_object_or_404(Grocery, pk=pk)
    return render(request, 'blog/grocery_detail.html', {'post': post})
