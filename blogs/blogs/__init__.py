# -*- coding: utf-8 -*-

"""
Created on 2024-03-21
:author: blogs (jobetcasquejo221@gmail.com)
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('blogs')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                blogs.kotti_configure

        to enable the ``blogs`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' blogs'
    settings['kotti.alembic_dirs'] += ' blogs:alembic'
    settings['kotti.available_types'] += ' blogs.resources.CustomContent'
    settings['kotti.fanstatic.view_needed'] += ' blogs.fanstatic.css_and_js'
    File.type_info.addable_to.append('CustomContent')


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('blogs:locale')
    config.add_static_view('static-blogs', 'blogs:static')

    config.scan(__name__)
