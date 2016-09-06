from django.db import models
from django.utils import timezone
from django import forms

class ParsedPage(models.Model):
  url = models.CharField(max_length=50, blank=True)
  page_description = models.CharField(max_length=50, blank=True)
  page_author = models.CharField(max_length=50, blank=True)
  page_date = models.CharField(max_length=50, blank=True)

  page_polarity = models.CharField(max_length=50, blank=True)
  page_subjectivity = models.CharField(max_length=50, blank=True)
  page_related_confidence_numbers = models.CharField(max_length=50, blank=True)

  def __unicode__(self):
    return self.page_title


class UrlForm(forms.ModelForm):

  class Meta:
    model = ParsedPage
    fields = ('url',)