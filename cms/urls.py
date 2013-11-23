# -*- coding: utf-8 -*-
from cms.apphook_pool import apphook_pool
from cms.views import details
from django.conf import settings
from django.conf.urls import url, patterns

reg_re = r'^(?u)(?P<slug>[-.//\w]+)%s$' % (settings.APPEND_SLASH and '/' or '')
reg = url(reg_re, details, name='pages-details-by-slug')

urlpatterns = [
    # Public pages
    url(r'^$', details, {'slug':''}, name='pages-root'),
    reg,
]

if apphook_pool.get_apphooks():
    """If there are some application urls, add special resolver, so we will
    have standard reverse support.
    """
    from cms.appresolver import get_app_patterns
    urlpatterns = get_app_patterns() + urlpatterns
    
urlpatterns = patterns('', *urlpatterns)
