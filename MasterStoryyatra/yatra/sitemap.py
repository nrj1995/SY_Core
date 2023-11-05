from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost

class postsitemap(Sitemap):
    changefriq = "monthly"
    priority = 0.9
    def items(self):
        return BlogPost.objects.all()
    

class staticpagegsitemap(Sitemap):
    changefriq = "monthly"
    priority = 0.9
    def items(self):
        return ['index','about','get_state_blog']
    def location(self, item):
        return reverse(item)


    
    
