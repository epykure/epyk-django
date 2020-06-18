"""
This example is just coming from the official Django website

https://docs.djangoproject.com/en/3.0/intro/tutorial01/
"""

from django.http import HttpResponse
from django.shortcuts import render

from epyk.core.Page import Report

import templates


def index(request):
  """
  Description:
  ------------
  Basic example using a Jinja template.
  Variable to finalise the template will be defined in this function.

  Thus the final template used to display the page will be build in two steps.
    - From Epyk to generate the HTML, JavaScript and CSS data
    - From Jinja to add the extra variables.

  Attributes:
  ----------
  :param request:
  """
  if request.GET.get('refresh') == 'Y':
    templates.refresh('index')

  return render(request, 'views/index.html', {'name': 'Test'})


def viewer(request, name):
  """
  Description:
  ------------
  Generic viewer to load bespoke based on name.

  Attributes:
  ----------
  :param request:
  :param name: String. The report name
  """
  if request.GET.get('refresh') == 'Y':
    templates.refresh(name)

  return render(request, 'views/%s.html' % name, {})


def chart(request):
  """
  Description:
  ------------
  Example of report using Plotly and Goe charts

  Attributes:
  ----------
  :param request:
  """
  return render(request, 'views/chart.html', {})


def dynamic(request):
  """
  Description:
  ------------
  Dynamic report automatically generated in the view.

  no template used here

  Attributes:
  ----------
  :param request:
  """
  page = Report()
  page.headers.dev()
  div = page.ui.div("Hellow World!")
  button = page.ui.button("Click Me")
  div.style.css.color = 'red'
  button.click([
    page.js.alert("Clicked")
  ])
  return HttpResponse(page.outs.html())
