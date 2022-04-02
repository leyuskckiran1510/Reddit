import requests as req
from PIL import Image
import numpy as np
import bin
import time

TOKEN = "".strip() # Your token here
# How to get this token
# 1. Go to https://www.reddit.com/r/place/
# 2. "Ctrl + Shift + I" to open the dev tools
# 3. Click on the "Network" tab
# 4. Click on the "Headers" tab
# 5. Copy the "Authorization" header
# 6. Paste it here after Bearer


url = "https://gql-realtime-2.reddit.com/query"




# canvas Size 999*999 location to start from
cord_x = 15
cord_y = 16
color = ''


def draw(TOKEN,x,y,color):
    data = {"operationName": "setPixel",
            "variables":
                {"input": {"actionName": "r/replace:set_pixel", "PixelMessageData":
                    {"coordinate": {"x": cord_x+x, "y": cord_y+y},
                     "colorIndex": color, "canvasIndex": 0}}},
            "query": "mutation setPixel($input: ActInput!) {\n  act(input: $input) {\n    data {\n      ... on BasicMessage {\n        id\n        data {\n          ... on GetUserCooldownResponseMessageData {\n            nextAvailablePixelTimestamp\n            __typename\n          }\n          ... on SetPixelResponseMessageData {\n            timestamp\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
    headers = {'authority': 'gql-realtime-2.reddit.com', 'method': 'POST', 'path': '/query', 'scheme': 'https',
               'accept': '*/*', 'accept-encoding': 'utf-8', 'accept-language': 'en-US,en;q=0.9',
               'apollographql-client-name': 'mona-lisa', 'apollographql-client-version': '0.0.1',
               'authorization': f'Bearer {TOKEN}', 'content-length': '666',
               'content-type': 'application/json', 'dnt': '1', 'https': '//hot-potato.reddit.com/',
               'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'sec-gpc': '1',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
    r = req.post(url, json=data, headers=headers)
    print(r.text)


def get_image_data():
    a = bin.Run()
    return a.evaluate_image()


def main():
    data = get_image_data()
    for x,n in enumerate(data):
        for y,color in enumerate(n):
            draw(TOKEN,x,y,color)
            time.sleep(5*60)


if __name__ == '__main__':
    main()
