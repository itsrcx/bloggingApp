from django.utils.text import slugify
import random
import string

def generateRandomStr(n):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    return res

def generateSlug(text):
    new_slug = slugify(text)
    from .models import Post
    if Post.objects.filter(slug = new_slug).exists():
        return generateSlug(text +'-'+ generateRandomStr(3))
    return new_slug
