from django import template
from yatra.models import Comment

register = template.Library()

@register.filter
def filter_comments(comments):
    return comments.filter(parent_comment__isnull=True)

@register.filter
def filter_replies(replies):
    return replies.order_by('-created_at')