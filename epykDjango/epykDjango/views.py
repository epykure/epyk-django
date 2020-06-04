"""
This example is just coming from the official Django website

https://docs.djangoproject.com/en/3.0/intro/tutorial01/
"""


from django.shortcuts import render


def index(request):
  """
  Basic example using a Jinja template

  :param request:
  """
  return render(request, 'views/index.html', {'name': 'Test'})


def chart(request):
  """

  :param request:
  """
  return render(request, 'views/chart.html', {})
