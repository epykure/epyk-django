
import os
import sys

sys.path.append(os.path.join("..", '..', '..', '..', 'epyk-ui'))

from epyk.core.Page import Report

rptObj = Report()
rptObj.headers.dev()

rptObj.ui.div("Hellow World {{ name }}!")

rptObj.outs.html_file(path=os.path.join("..", "..", 'views', 'templates', 'views'), name=os.path.split(os.path.abspath(__file__))[-1][:-3])

