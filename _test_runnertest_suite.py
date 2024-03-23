import unittest
from main import *

# Add imports here
from django.test import TestCase
from models import CustomStylePluginModel

class UnitTests(unittest.TestCase):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.plugin = None
  

  def setUp(self):
      self.plugin = CustomStylePluginModel.objects.create(
        heading_size="h1",
        paragraph_size="normal",
        heading_class="custom-heading",
        paragraph_class="custom-paragraph",
      )
    

  def tearDown(self):
      self.plugin.delete()

  def test_test_plugin(self):
      self.assertEqual(self.plugin.header_size, "h1")
      self.assertEqual(self.plugin.paragraph_size, "normal")
      self.assertEqual(self.plugin.heading_class, "custom-heading")
      self.assertEqual(self.plugin.paragraph_class, "custom-paragraph")

