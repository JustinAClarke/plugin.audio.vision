# https://docs.python.org/2.7/
import os
import sys
import urllib
import urlparse
# http://mirrors.kodi.tv/docs/python-docs/
import xbmcaddon
import xbmcgui
import xbmcplugin

def build_url(query):
    base_url = sys.argv[0]
    return base_url + '?' + urllib.urlencode(query)
    
def build_song_list():
    '''
    Vision      64k     https://streams2.vision.org.au/vision.mp3
    Vision180   128k    https://streams2.vision.org.au/vision180-128k.aac
    Vision180   64k     https://streams2.vision.org.au/vision180-64k.mp3
    '''
    song_list = []
    #vision
    li = xbmcgui.ListItem(label='Vision Christian Radio 64k',thumbnailImage='https://vision.org.au/wp-content/themes/visionmedia/images/vision-logo.png')
    li.setProperty('IsPlayable', 'true')
    li.setProperty('fanart_image', 'https://vision.org.au/wp-content/themes/visionmedia/images/vision-logo.png')
    url = build_url({'mode': 'stream', 'url': 'https://streams2.vision.org.au/vision.mp3', 'title': 'Vision Christian Radio 64k'})
    song_list.append((url, li, False))
    
    #vision180
    li = xbmcgui.ListItem(label='Vision180 Radio 128k',thumbnailImage='http://vision180.org.au/wp-content/themes/vision180/images/vision-logo.png')
    li.setProperty('IsPlayable', 'true')
    li.setProperty('fanart_image', 'http://vision180.org.au/wp-content/themes/vision180/images/vision-logo.png')
    url = build_url({'mode': 'stream', 'url': 'https://streams2.vision.org.au/vision180-128k.aac', 'title': 'Vision180 Radio 128k'})
    song_list.append((url, li, False))
    li = xbmcgui.ListItem(label='Vision180 Radio 64k',thumbnailImage='http://vision180.org.au/wp-content/themes/vision180/images/vision-logo.png')
    li.setProperty('IsPlayable', 'true')
    li.setProperty('fanart_image', 'http://vision180.org.au/wp-content/themes/vision180/images/vision-logo.png')
    url = build_url({'mode': 'stream', 'url': 'https://streams2.vision.org.au/vision180-64k.mp3', 'title': 'Vision180 Radio 64k'})
    song_list.append((url, li, False))
    
    '''
    song_list = []
    # iterate over the contents of the dictionary songs to build the list
    for song in songs:
        # create a list item using the song filename for the label
        li = xbmcgui.ListItem(label=songs[song]['title'], thumbnailImage=songs[song]['album_cover'])
        # set the fanart to the albumc cover
        li.setProperty('fanart_image', songs[song]['album_cover'])
        # set the list item to playable
        li.setProperty('IsPlayable', 'true')
        # build the plugin url for Kodi
        # Example: plugin://plugin.audio.example/?url=http%3A%2F%2Fwww.theaudiodb.com%2Ftestfiles%2F01-pablo_perez-your_ad_here.mp3&mode=stream&title=01-pablo_perez-your_ad_here.mp3
        url = build_url({'mode': 'stream', 'url': songs[song]['url'], 'title': songs[song]['title']})
        # add the current list item to a list
        song_list.append((url, li, False))
    '''
    # add list to Kodi per Martijn
    # http://forum.kodi.tv/showthread.php?tid=209948&pid=2094170#pid2094170
    xbmcplugin.addDirectoryItems(addon_handle, song_list, len(song_list))
    # set the content of the directory
    xbmcplugin.setContent(addon_handle, 'songs')
    xbmcplugin.endOfDirectory(addon_handle)
    
def play_song(url):
    # set the path of the song to a list item
    play_item = xbmcgui.ListItem(path=url)
    # the list item is ready to be played by Kodi
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)
    
def main():
    args = urlparse.parse_qs(sys.argv[2][1:])
    mode = args.get('mode', None)
    
    # initial launch of add-on
    if mode is None:

        # display the list of songs in Kodi
        build_song_list()
    # a song from the list has been selected
    elif mode[0] == 'stream':
        # pass the url of the song to play_song
        play_song(args['url'][0])
    
if __name__ == '__main__':
    addon_handle = int(sys.argv[1])
    main()
