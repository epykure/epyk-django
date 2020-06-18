

def get_page(rptObj):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param rptObj:

  :rtype: epyk.core.Page.Report
  """
  rptObj.headers.dev()
  rptObj.ui.div("Hellow World {{ name }}!")
  return rptObj


