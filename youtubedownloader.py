from pytube import YouTube

print("hello user od youtube downloader")


def video_downloader(video_url):
   
    my_video = YouTube(video_url)
    
    my_video.streams.get_highest_resolution().download()
    
    return my_video.title

try:
    
    youtube_link = input('Enter the YouTube link:')
    print(f'Downloading your Video, please wait.......')
    
    video = video_downloader(youtube_link)
    
    print(f'"{video}" downloaded succussfully!!')

except:
    print(f'Failed to download video\nThe '\
          'following might be the causes\n->No internet '\
          'connection\n->Invalid video link')
