import youtube_dl

def downloadYoutubeFromUrl(url):
    ydl_opts = {'nocheckcertificate':True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
