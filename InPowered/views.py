from django.shortcuts               import render, get_object_or_404
from django.utils                   import timezone
from django.template                import loader
from django.http                    import HttpResponseRedirect, HttpResponse
from aylienapiclient                import textapi
from django.conf                    import settings
from aylienapiclient                import textapi
from .models                        import ParsedPage, UrlForm

import datetime



# Should be in settings.py but for some reason, Django did not recognize settings.X_AYLIEN_TextAPI_Application_ID nor settings.X_AYLIEN_TextAPI_Application_Key

X_AYLIEN_TextAPI_Application_ID = "51c39653"
X_AYLIEN_TextAPI_Application_Key = 'e1a6d9e87dfd26bf5eb3dd2571c3c999'


def index(request):
  context = {
    'welcome_message': 'Welcome To Your Favorite URL Parser'
  }

  return render(request, 'InPowered/index.html', context)

def parse_url(request):
  client = textapi.Client(X_AYLIEN_TextAPI_Application_ID, X_AYLIEN_TextAPI_Application_Key)

  url = request.POST['url']
  extract = client.Extract({"url": url})
  page_author = extract['author']
  page_description = extract['title']
  page_publish_date = extract['publishDate']

  classifications = client.Classify({"url": url})
  url_confidence_number = classifications['categories'][0]['confidence']
  url_text = classifications['text']

  url_text_sentiment = client.Sentiment({'text': url_text})
  url_text_polarity = url_text_sentiment['polarity']
  url_text_subjectivity_confidence = url_text_sentiment['subjectivity_confidence']
  url_text_subjectivity = url_text_sentiment['subjectivity']

  context = {
    'url_text_polarity' :url_text_polarity,
    'url_text_subjectivity': url_text_subjectivity,
    'url_text_subjectivity_confidence': url_text_subjectivity_confidence,
    'url': url
  }

  parsedPage = ParsedPage(page_date=page_publish_date, page_author=page_author, page_description=page_description, page_polarity=url_text_polarity, page_subjectivity=url_text_subjectivity, page_related_confidence_numbers=url_confidence_number, url=url)

  parsedPage.save()

  return render(request, 'InPowered/results.html', context)
