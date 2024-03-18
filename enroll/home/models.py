from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel

class HomePage(Page):

  image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+',
    help_text = "Homepage" 
  )

  hero_text = models.CharField(
    blank=True,
    max_length=255, help_text="Sample Site",
  )
  hero_cta = models.CharField(
    blank=True,
    verbose_name="Call to Action",
    max_length=255,
    help_text="Sample Site",
  )
  hero_cta_link = models.ForeignKey(
    "wagtailcore.Page",
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name="+",
    verbose_name="Hero CTA link",
    help_text="Choose a page to link to for the Call to Action",
  )

  body = RichTextField(blank=True)

  content_panels = Page.content_panels + [
      MultiFieldPanel(
          [
              FieldPanel("image"),
              FieldPanel("hero_text"),
              FieldPanel("hero_cta"),
              FieldPanel("hero_cta_link"),
          ],
          heading="Hero section",
      ),
      FieldPanel('body'),
  ]
