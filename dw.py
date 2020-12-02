from pytube import YouTube
from tkinter import *

'''
Documentation: https://pypi.org/project/pytube/
'''
###--- Individual videos ---###

link = "https://www.youtube.com/watch?v=HHBsvKnCkwI"

try:
    youtube = YouTube(link)
except:
    print("Connection error")

print(youtube.title)
print(youtube.video_id)
print(youtube.thumbnail_url)
print(youtube.views)

stream = youtube.streams.first()
stream.download()

# SAVE_PATH = "E:/"

# link = "https://www.youtube.com/watch?v=HHBsvKnCkwI"

# try:
#     youtube = YouTube(link)
# except:
#     print("Connection error")

# stream = youtube.streams.first()
# stream.download()

# root = Tk()

# root.geometry("500x350")

# root.title("Download YouTube Videos.")

# def dw():
#     '''
#     Download youtube videos without errors
#     '''
#     try:
#         myVar.set("DOWNLOADING...")
#         root.update()
#         YouTube(link.get()).streams.first().download()
#         link.set("Download successful.")
#     except:
#         myVar.set("Error found...")
#         root.updated()
#         link.set("Enter correct link")

# Label(root, text="Welcome to Youtube\nDownloader")
# myVar = StringVar()
# myVar.set("Enter a url below:")
# Entry(root, textvariable=myVar, width=40).pack(pady=10)
# link = StringVar()
# Entry(root, textvariable=link, width=40).pack(pady=10)
# Button(root, text="Download", command=dw).pack()
# root.mainloop()


###--- Playlists ---###
# yt = YouTube('[...]')
# yt.streams.get_highest_resolution().download()

# # or simply
# pl = Playlists('[..]')
# pl.download_all
