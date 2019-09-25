import urllib.request
import json
import requests
import re

#look into urllib.parse for urls instead of the ugly regex

def main():
    clip_url = input('Please enter the link of the clip(embed links not supported): ')
    clip_name = input('Enter the name for the clip to be saved as: ')

    if not clip_name:
        clip_name = 'clip.mp4'
    else:
        clip_name = clip_name + '.mp4'

    try:
        clip_id = re.findall(r"^((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$", clip_url)[0][5]
    except Exception as e:
        print(e)

    url = 'https://clips.twitch.tv/api/v2/clips/' + clip_id + '/status'
    r = requests.get(url)
    data = json.loads(r.content.decode('utf-8'))
    vid_link = data['quality_options'][0]['source']

    try:
        print("Downloading starting...\n")
        urllib.request.urlretrieve(vid_link, clip_name)
        print("Download completed!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()