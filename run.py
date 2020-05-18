from __future__ import unicode_literals

from downloadYoutubeFromUrl import downloadYoutubeFromUrl
from parseWebpageForYoutubeLinks import getYoutubeLinks

def main():
    print('Started...')
    getYoutubeLinks("https://youtubehindivideos.com/ramayan-serial-youtube/", "https://www.youtube.com/watch")
    file = open("youtubeLinks.txt", "r")
    links = file.read().split()
    print(links)
    # downloadYoutubeFromUrl(links)

if __name__ == "__main__":
    main()