# -*- coding: utf-8 -*-

"""
Created on 2024-03-21
:author: blogs (jobetcasquejo221@gmail.com)
"""

from pyramid.view import view_config
from pyramid.view import view_defaults

from blogs import _
from blogs.resources import CustomContent
from blogs.fanstatic import css_and_js
from blogs.views import BaseView


@view_defaults(context=CustomContent, permission='view')
class CustomContentViews(BaseView):
    """ Views for :class:`blogs.resources.CustomContent` """

    @view_config(name='view', permission='view',
                 renderer='blogs:templates/custom-content-default.pt')
    def default_view(self):
        """ Default view for :class:`blogs.resources.CustomContent`

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        return {
            'foo': _(u'bar'),
        }

    @view_config(name='alternative-view', permission='view',
                 renderer='blogs:templates/custom-content-alternative.pt')
    def alternative_view(self):
        """ Alternative view for :class:`blogs.resources.CustomContent`.
        This view requires the JS / CSS resources defined in
        :mod:`blogs.fanstatic`.

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        css_and_js.need()

        return {
            'foo': _(u'bar'),
        }
