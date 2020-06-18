
from epyk.tests import data_urls


def get_page(rptObj):
  """

  Attributes:
  ----------
  :param rptObj:

  :rtype: epyk.core.Page.Report
  """
  records = [
    {'countries': 'FRA', 'size': 20},
    {'countries': 'GBR', 'size': 50},
    {'countries': 'DEU', 'size': 30},
    {'countries': 'RUS', 'size': 15},
    {'countries': 'ESP', 'size': 15},
  ]

  data_countries = rptObj.py.requests.csv(data_urls.PLOTLY_COUNTRIES)

  europe = rptObj.ui.geo.plotly.choropleths.europe(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
  asia = rptObj.ui.geo.plotly.choropleths.asia(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
  africa = rptObj.ui.geo.plotly.choropleths.africa(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
  sa = rptObj.ui.geo.plotly.choropleths.south_america(data_countries, size_col='GDP (BILLIONS)', country_col='CODE')
  na = rptObj.ui.geo.plotly.choropleths.north_america(data_countries, size_col='GDP (BILLIONS)', country_col='CODE', height=(600, 'px'))

  rptObj.ui.button("Click").click([
    europe.build(rptObj.data.plotly.choropleth(records, 'countries', 'size'))
  ])

  rptObj.ui.grid([
    [na],
    [europe, asia],
    [africa, sa],
  ])


