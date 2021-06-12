from pytube import YouTube
import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from download import *
from upload import upload_video

# enter url in download.py

print("With Great Power comes Great Responsibility")
download_vid()
upload_video()
