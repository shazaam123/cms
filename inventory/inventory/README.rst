django CMS Link
pypi build coverage

django CMS Link is a plugin for django CMS that allows you to add links on your site.

This plugin supports child plugins. If you add an other plugin as a child it will take this content instead of the link name as the content of the link.

This addon is compatible with Divio Cloud and is also available on the django CMS Marketplace for easy installation.

preview.gif

Contributing
This is a an open-source project. We'll be delighted to receive your feedback in the form of issues and pull requests. Before submitting your pull request, please review our contribution guidelines.

We're grateful to all contributors who have helped create and maintain this package. Contributors are listed at the contributors section.

One of the easiest contributions you can make is helping to translate this addon on Transifex.

Documentation
See REQUIREMENTS in the setup.py file for additional dependencies:

python django djangocms

Django Filer 1.7 or higher
Make sure django Filer is installed and configured appropriately.

Installation
For a manual install:

run pip install djangocms-link
add djangocms_link to your INSTALLED_APPS
run python manage.py migrate djangocms_link
Configuration
Note that the provided templates are very minimal by design. You are encouraged to adapt and override them to your project's requirements.

This addon provides a default template for all instances. You can provide additional template choices by adding a DJANGOCMS_LINK_TEMPLATES setting:

DJANGOCMS_LINK_TEMPLATES = [
    ('feature', _('Featured Version')),
]
You'll need to create the feature folder inside templates/djangocms_link/ otherwise you will get a template does not exist error. You can do this by copying the default folder inside that directory and renaming it to feature.

To support environments where non-standard URLs would otherwise work, this project supports the defining of an additional RegEx pattern for validating the host-portion of the URL.

For example:

# RFC1123 Pattern:
DJANGOCMS_LINK_INTRANET_HOSTNAME_PATTERN = r'[a-z,0-9,-]{1,15}'
Either of these might accept a URL such as:

http://SEARCHHOST/?q=some+search+string
If left undefined, the normal Django URLValidator will be used.

Django Select2
This plugin supports django-select2 for simpler use of internal links. You need to manually enable it by:

run pip install django-select2
add django_select2 to your INSTALLED_APPS
add url(r'^select2/', include('django_select2.urls')), to your urls.py
set DJANGOCMS_LINK_USE_SELECT2 = True in your settings.py
Running Tests
You can run tests by executing:

virtualenv env
source env/bin/activate
pip install -r tests/requirements.txt
python setup.py test
Updating from cmsplugin-filer
Historically, cmsplugin-filer was used to create file, folder, image, link, teaser & video plugins on your django CMS projects. Now cmsplugin-filer has been archived, you can still migrate your old instances without having to copy them manually to the new djangocms-<file|picture|link|...> plugins.

There's a third-party management command that supports your migration:

migrate_cmsplugin_filer.py

This management command is only a starting point. It has worked out of the box for some people, but we encourage you to read the code, understand what it does, and test it on a development environment before running it on your production server.

The management command is only configured to transfer your cmsplugin_link, cmsplugin_file, cmsplugin_folder and cmsplugin_image plugins to modern djangocms_* plugins. If you need to transfer other cmsplugin_* plugins, you'll have to write your own code.

Alternatively you can use the deprecate_cmsplugin_filer app, which only adds a small migration that transfer the old cmsplugin-filer plugins instances to the new djangocms-<file|picture|link|...> plugins.