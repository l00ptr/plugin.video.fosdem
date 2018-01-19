import requests
from xml.etree import ElementTree
def get_video_list():
   """
   This function build a complete list of all 
   video on this channel. If the request to
   the conf website doesn't work or if empty
   it will return None. Otherwise the response
   should be parsed and transformed into a 
   dictionnary.
   """
   video_list  = {}
   try:
       response = requests.get('https://fosdem.org/2017/schedule/xml')
       xml_tree = ElementTree.fromstring(response.content)
       events = xml_tree.findall('.//event')
       for a_event in events:
           #for print a_event.value
           room = a_event.find('room').text
           title = a_event.find('title').text
           track = a_event.find('track').text
           slug = a_event.find('slug').text
           links = a_event.findall('.//link')
           for a_link in links:
	      a_link_href = a_link.attrib['href']
	      is_valid_link = all(a_word in 
                                  a_link_href for a_word 
                                  in ['.mp4',
                                      'fosdem',
                                      'video'])
              if is_valid_link:
                  print a_link_href
                  video_list[slug] = {
			              'room': room,
	                              'title': title,
		                      'track': track,
                                      'link' : a_link_href 
                                     } 
	

   except requests.RequestException:
       pass 
   return video_list

def get_video_data():
   pass
