#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib,json
url = "http://211.139.123.188:18088/sq_api/api"
data = {
  "cmd": "staticData",
  "params": {
    "dataType": "1"
  }
}
req = urllib2.Request(url, json.dumps(data))
resp = urllib2.urlopen(req)
res = resp.read()
print res
