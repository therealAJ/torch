import config
import httplib 
import urllib 
import base64


# #### HTTP Headers + Encoding the URL

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': config.api_key
}

params = urllib.urlencode ({
        ## I will tweak these lolssss
        'visualFeatures': 'Categories',
        'language': 'en'
    })


# #### Image URL and API Call

body = "{'url': 'https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg'}"

try: 
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.message, e.message))