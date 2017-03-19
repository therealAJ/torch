import httplib, urllib, base64
import config
import json


def read(filepath):
    file = open(filepath, 'rb').read()
    files = {'file': file}

    headers = {
        # Request headers. Replace the key below with your subscription key.
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': config.api_key
    }

    params = urllib.urlencode({
        # Request parameters. The language setting "unk" means automatically detect the language.
        'language': 'unk',
        'detectOrientation ': 'true',
    })

    # Replace the three dots below with the URL of a JEPG image containing text.
    body = file

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        json_data = json.loads(data)
        lines = json_data['regions'][0]['lines']
        text = []
        sentence = ""
        for line in lines:
            words = line['words']
            for word in words:
                text.append(str(word['text']))
                #print(word['text'])
        sentence = " ".join(text)
        print sentence
        conn.close()
        return sentence
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
