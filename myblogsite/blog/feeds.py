import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = 'CHOBOITech blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of CHOBOITech blog.'

    def items(self):
        return Post.published.all()[:5]
