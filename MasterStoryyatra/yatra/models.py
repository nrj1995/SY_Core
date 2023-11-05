from django.db import models
from django.urls import reverse

# from ckeditor.fields import RichTextUploadingField 
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class BlogPost(models.Model):

    Nation = models.CharField(max_length=50,blank=True, null=True)

    state =  models.CharField(max_length=50,blank=True, null=True)

    title = models.CharField(max_length=200)

    description = models.CharField(max_length=400, null=True)

    author = models.CharField(max_length=100, null=True)

    content = RichTextUploadingField()

    date_posted = models.DateTimeField(auto_now_add=True)

    photo_1 = models.ImageField(upload_to='blog_photos/', blank=True, null=True)

    photo_2 = models.ImageField(upload_to='blog_photos/', blank=True, null=True)

    photo_3 = models.ImageField(upload_to='blog_photos/', blank=True, null=True)

    # Add field to store number of likes

    likes = models.IntegerField(default=0)

 

    def __str__(self):

        return f"blog name- {self.title} uploaded on {str(self.date_posted)}"

    def get_absolute_url(self):
      return reverse('detailed_blog', args=[str(self.id)])
      
      
        

# class BlogPst(models.Model):

#     title = models.CharField(max_length=255)

#     content = RichTextField()

#     pub_date = models.DateTimeField(auto_now_add=True)
 
class Comment(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE,related_name='comments')
   text = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
#    ---parent comment--
   parent_comment = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')

#    def replies(self):
#     return Comment.objects.filter(blog=self.blog, parent_comment=self).order_by('-created_at')

   def __str__(self):
    return self.name


