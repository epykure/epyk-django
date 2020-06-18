
import os
import sys

from epyk.core.Page import Report

template_path = os.path.join('epykDjango', 'epykDjango', 'reports')
sys.path.append(template_path)


def refresh(view_name):
  """
  Description:
  ------------
  This will transpile only the selected report.
  Transpilation will generate HTML content from the python code using Epyk framework

  Attributes:
  ----------
  :param view_name:
  """
  mod = __import__(view_name)
  page = Report()
  mod.get_page(page)
  print(page.outs.html_file(path=os.path.join("epykDjango", 'views', 'templates', 'views'), name=view_name))


if __name__ == '__main__':
  """
  This will transpile all the reports in the reports folder
  """
  for report in os.listdir(template_path):
    if report.endswith(".py"):
      view_name = report[:-3]
      mod = __import__(view_name)
      page = Report()
      mod.get_page(page)
      print(page.outs.html_file(path=os.path.join("epykDjango", 'views', 'templates', 'views'), name=view_name))
