# -*- coding: utf-8 -*-

"""
Created on 2024-03-21
:author: blogs (jobetcasquejo221@gmail.com)
"""

from pytest import fixture


@fixture
def dummy_content(root):

    from blogs.resources import CustomContent

    root['cc'] = cc = CustomContent(
        title=u'My content',
        description=u'My very custom content is custom',
        custom_attribute='Lorem ipsum'
    )

    return cc


def test_view(dummy_content, dummy_request):

    from blogs.views.view import CustomContentViews

    views = CustomContentViews(dummy_content, dummy_request)

    default = views.default_view()
    assert 'foo' in default

    alternative = views.alternative_view()
    assert alternative['foo'] == u'bar'
