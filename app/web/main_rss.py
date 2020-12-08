from django.core import rss
from django.models.core import sites

# these are entries of my blog
from django.models.blog import documents

blog_document_feed = rss.FeedConfiguration(
    slug = 'blog',
    title_cb = lambda param: "I Can't Believe It's Blog!",
    link_cb = lambda param: 'http://%s/blog/' % sites.get_current().domain,
    description_cb = lambda param: 'The Great Example of Why 99.999% of Blogs Suck',
    get_list_func_cb = lambda param: documents.get_list,
    get_list_kwargs = {
        'limit': 10,
    }
)

rss.register_feed(blog_document_feed)
