import datetime
import time

from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from download import *
import os


def upload_video():
    print(f'Uploading {yt_obj.title}')
    CLIENT_SECRET_FILE = 'googleAPI.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    now = datetime.datetime.now()
    upload_date_time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute,
                                         int(now.second)).isoformat() + '.000Z'
    request_body = {
        'snippet': {
            'categoryI': 23,
            'title': f'{yt_obj.title}',
            'description': 'Like Share and Subscribe for more \n thanks :)',
            'tags': ['not so funny', 'wakanda forever']
        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': False
    }
    mediaFile = MediaFileUpload('yt_video.mp4')

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()
    print("Upload successful Wakanda Forever")
    print("Waiting for 10 seconds")
    time.sleep(10)
    try:
        os.remove('yt_video.mp4')
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    print("Removed temp files!")
