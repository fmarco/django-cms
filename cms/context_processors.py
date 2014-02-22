# -*- coding: utf-8 -*-
from django.utils.functional import SimpleLazyObject
from cms.utils.conf import get_cms_setting
from cms.utils import get_template_from_request
import warnings
import functools


def cms_settings(request):
    """
    Adds cms-related context variables to the context.
    """
    return {
        'CMS_MEDIA_URL': get_cms_setting('MEDIA_URL'),
        'CMS_TEMPLATE': SimpleLazyObject(
            lambda: get_template_from_request(request)),
    }


def media(request):
    warnings.warn('cms.context_processors.media has been deprecated in favor of'
                  'cms.context_processors.cms_settings. Please update your'
                  'configuration', DeprecationWarning)
    return cms_settings(request)
