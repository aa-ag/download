from pytube import YouTube

'''
Documentation: https://pypi.org/project/pytube/
'''

SAVE_PATH = "E:/"

link = "https://www.youtube.com/watch?v=HHBsvKnCkwI"

try:
    youtube = YouTube(link)
except:
    print("Connection error")

stream = youtube.streams.first()
stream.download()