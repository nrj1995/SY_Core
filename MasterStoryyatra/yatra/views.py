from django.shortcuts import render
from yatra.models import *
from StoryYatra import settings

from django.shortcuts import get_object_or_404
from django.http import JsonResponse  
from django.shortcuts import redirect  
from django.db.models import Q
from .forms import *
from django.utils.html import strip_tags
import re
 
# Create your views here.



def index(request):
    blog = BlogPost.objects.order_by('-id')[:3]
    liked_blog = list(BlogPost.objects.order_by('-likes')[:3])
    ccount=[Comment.objects.filter(blog=i.id,parent_comment__isnull=True).count() for i in liked_blog ]
    top_liked_blog=list(zip(liked_blog,ccount))
    print(top_liked_blog[0][0].title)
    # blog1 = BlogPost.objects.last()
    # contstr = strip_tags(blog1.content).replace('&nbsp;','').strip()
    # refstr = re.sub(' +', ' ', contstr)
    # print("ref strjjjjjjjj--",refstr[:100])
    # clean_text = "\n".join([line for line in refstr.split("\n") if line.strip() != ""])
    # print("clean datrrjn---",clean_text)
    # print(blog[0].photo_1)
    # print(settings.MEDIA_ROOT)
    media=settings.MEDIA_ROOT
    # print("bfjdfnfd",blog1[0].content)
    return render(request, "index.html",{'blog':blog,'liked_blog':top_liked_blog,'media':media})

def about(request):
    return render(request, "about.html")    

def detailed_blog_view(request, id):
    blog_data = BlogPost.objects.get(id=id)
    comments = blog_data.comments.all().order_by('-created_at')
    print("comments are ",comments)
    # comments = Comment.objects.filter(blog=id).order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        # if comment_form.cleaned_data.get('email') =="":
        #     print('yes------------')
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog= blog_data
            new_comment.save()
            return redirect('detailed_blog',id=blog_data.id)
    # else:
    #     comment_form = CommentForm()

    return render(request, "blogdet.html",{'blog_data':blog_data,'comments':comments})

def likecount(request,post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    post.likes += 1

    post.save()

    return JsonResponse({'likes': post.likes})

def create_post(request):

    if request.method == 'POST':

        form = BlogPostForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = BlogPostForm()

    return render(request, 'create_post.html', {'form': form})

# def post_comment(request,post_id):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         comment = request.POST.get('body')
#         blog = BlogPost.objects.get(id=post_id)
#         com = Comment.objects.create(name=name,email=email,blog=blog,text=comment)
#         commethtml = '<li class="comment"><div class="comment-author">'+com.name+'</div><div class="comment-date">'+str(com.created_at)+'</div><div class="comment-text">'+com.text+'</div></li>'
#         return JsonResponse({'success': True,'comment': commethtml})

# ---------Function for Search result------------------
def search(request):
    query = request.GET.get('q')
    
    results = []
    if query:
        results = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query)
        )
    context = {'results': results,'query': query,'searchCount':len(results)}
    return render(request, 'search_results.html', context) 

# ----------function for Reply comment-------
def reply_comment(request, comment_id):
    # Get the parent comment object
    parent_comment = get_object_or_404(Comment, pk=comment_id)
    print(parent_comment.replies.all())
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print("i am here....")
        if form.is_valid():
            # Create a new comment object with the parent comment set to the specified ID
            comment = form.save(commit=False)
            comment.blog = parent_comment.blog
            comment.parent_comment = parent_comment
            comment.save()
            return redirect('detailed_blog', id=parent_comment.blog.pk)
    
    # return render(request, 'myapp/comment_reply.html', {'form': form})

def navbar_data(request):
   nation_dist = BlogPost.objects.values('Nation').distinct()
   data = [i['Nation'] for i in nation_dist if i['Nation'] is not None]
   print(">>>>>>>>>>>>",data)
   return JsonResponse({'data':data})   

def NationDetails(request,cname):
    print("cname-->",cname)
    states =  BlogPost.objects.values('state').filter(Nation=cname).distinct()
    return render(request, 'state_blog.html',{'states': states})
   

def get_state_blog(request):
    if request.method == 'GET':
        state = request.GET.get('state')
        stateblogs = list(BlogPost.objects.filter(state=state).values())

        print('>>>>>>>><>>>>',stateblogs)
        return JsonResponse({'data':stateblogs})