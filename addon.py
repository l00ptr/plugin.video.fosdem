import sys
import xbmcgui
import xbmcplugin
import xbmcaddon
import routing
from resources.fosdem import get_video_list

plugin = routing.Plugin()
video_list = get_video_list()
criteria_l = ['room','track']
supported_year = ["2017"]

@plugin.route('/')
def show_index():
    for a_supported_year in supported_year:
        url = plugin.url_for(show_year,year=a_supported_year)
        li = xbmcgui.ListItem(a_supported_year)
        xbmcplugin.addDirectoryItem(plugin.handle, url, li, True)
    xbmcplugin.endOfDirectory(plugin.handle)

@plugin.route('/year/<year>')
def show_year(year):
    xbmcplugin.setContent(plugin.handle,'movies')
    for a_criteria in criteria_l:
        #pass
        li = xbmcgui.ListItem('Show video by {}'.format(a_criteria))
        url  = plugin.url_for(show_by_criteria,criteria=a_criteria, year=year)
        xbmcplugin.addDirectoryItem(plugin.handle, url, li, True)
    xbmcplugin.endOfDirectory(plugin.handle)

@plugin.route('/criteria/<criteria>/<year>')
def show_by_criteria(criteria, year):
    if criteria not in criteria_l:
        return None
    xbmcplugin.setContent(plugin.handle,'movies')
    items = set([a_video[criteria] for a_video in video_list.values()])
    for a_item in list(items):
        #pass
        li = xbmcgui.ListItem(a_item)
        url  = plugin.url_for(show_video_by_criteria,criteria=criteria,
                              selected_criteria_value=a_item, year=year)
        xbmcplugin.addDirectoryItem(plugin.handle,url,li, True)
    xbmcplugin.endOfDirectory(plugin.handle)
        
@plugin.route('/video_by_criteria/<criteria>/<selected_criteria_value>/<year>')
def show_video_by_criteria(criteria, selected_criteria_value, year):
    if criteria not in criteria_l:
        return None
    items = [a_video for a_video in video_list.values() \
             if a_video[criteria]==selected_criteria_value]
    print items
    for a_item in items:
        print a_item
        pass
        li = xbmcgui.ListItem(a_item['title'])
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(plugin.handle,a_item['link'],li)
        #xbmcplugin.addDirectoryItem(plugin.handle,'http://google.com',
    xbmcplugin.endOfDirectory(plugin.handle)
 

if __name__ == '__main__':
    plugin.run()
