# -*- coding: utf-8 -*-

"""
Created on 2024-03-21
:author: blogs (jobetcasquejo221@gmail.com)
"""

from pytest import mark


def test_login_required(webtest, root):
    resp = webtest.get('/add_custom_content')
    assert resp.status_code == 302


@mark.user('admin')
def test_add(webtest, root):

    resp = webtest.get('/add_custom_content')

    # submit empty form
    form = resp.forms['deform']
    resp = form.submit('save')
    assert 'There was a problem' in str(resp.body)

    # submit valid form
    form = resp.forms['deform']
    form['title'] = 'My Custom Content'
    form['custom_attribute'] = 'My Custom Attribute Value'
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in str(resp.body)


@mark.user('admin')
def test_edit(webtest, root):

    from blogs.resources import CustomContent

    root['cc'] = CustomContent(title=u'Content Title')

    resp = webtest.get('/cc/@@edit')
    form = resp.forms['deform']
    assert form['title'].value == u'Content Title'
    assert form['custom_attribute'].value == u''
    form['custom_attribute'] = u'Bazinga'
    resp = form.submit('save').maybe_follow()
    assert u'Your changes have been saved.' in str(resp.body)
    assert u'Bazinga' in str(resp.body)
