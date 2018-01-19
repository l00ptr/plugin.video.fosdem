import sys
import xbmcgui
import xbmcplugin
import xbmcaddon
from resources.fosdem import get_video_list

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'https://video.fosdem.org/2017/AW1.120/darpa_hackfest.mp4'


 
 

for a_video_slug, a_video in get_video_list().items():
    li = xbmcgui.ListItem(a_video['title'])
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=a_video['link'], listitem=li)
    print a_video_slug
xbmcplugin.endOfDirectory(addon_handle)
