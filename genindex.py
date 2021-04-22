#!/usr/bin/env python
import re
import urllib.request

template = '''
<!doctype html>
<html>
  <head>
    <title>Twilio OpenAPI Documentation</title>
    <style>
      body {
          text-align: center;
      }
      ul {
        list-style-type: none;
        display: flex;
        flex-wrap: wrap;
        padding-inline-start: 0;
      }
      li {
        display: block;
        margin: 10px;
        padding: 20px;
        border: 1px solid black;
        border-radius: 30px;
        background: #eef;
      }
      li:hover {
        background: #ccf;
      }
      a {
        text-decoration: none;
        font-size: 120%;
      }
    </style>
  </head>
  <body>
    <h1>Twilio OpenAPI Documentation</h1>
    <ul>

{PRODUCTS}
    </ul>
  </body>
</html>
'''

with urllib.request.urlopen('https://github.com/twilio/twilio-oai/tree/main/spec/json') as response:
   r = response.read()
apis = [api.decode() for api in re.findall(b'>twilio_([^\\"]*)\\.json', r)]

links = ''
for api in apis:
    product, version = api.rsplit('_v', 1)
    links += f'<li><a href=redoc.html?product={product}_v{version}>{product.title()} v{version}</a></li>\n'

print(template.strip().replace('{PRODUCTS}', links))
