from pytube import YouTube

url = 'https://youtu.be/StKxJsXXXEE'
yt_obj = YouTube(url)


def download_vid():
    try:
        c = f'{yt_obj.title}'
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        # download the highest quality video
        filters.get_highest_resolution().download(filename="yt_video")
        print(c + 'Downloaded Successfully')
        print()
    except Exception as e:
        print(e)
