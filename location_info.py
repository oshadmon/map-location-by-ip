import json 
import os
import requests

def __convert_json(json_obj:str): 
   """
   Given a JSON object, covert to dict 
   :args: 
      json_obj:str - json to convert to dict
   :return: 
      if success return dict of json_obj else return False 
   """
   try: 
      return json.loads(json_obj) 
   except Exception as e:    
      print('Failed to convert JSON (%s) to dict [Error: %s]' % (json_obj, e)) 
      return False 

def get_location(ip:str):
   """
   Based on the IP get location info
   :args: 
      ip:str - IP address with desired location 
   :param: 
      output:str - json value with location info 
   :return: 
      location info (as JSON), if fails return False 
   :sample: 
      {"ip":"45.79.66.203","country_code":"US","country_name":"United States","region_code":"CA","region_name":"California","city":"Fremont","zip_code":"94536","time_zone":"America/Los_Angeles","latitude":37.5625,"longitude":-122.0004,"metro_code":807}
   """
   try: 
      return os.popen('curl -X GET https://freegeoip.live/json/%s 2> /dev/null' %  ip).read().replace('\n', '')
   except Exception as e: 
      print('Failed to retrive location info based on ip % [Error: %s' % (ip, e)) 
      return False 

   return output.replace('\n','')

def get_address(ip:str): 
   """
   Based on an IP, eexecute get_location + return location address
   :args: 
      ip:str - IP to check 
   :param: 
      output:str - Value to reuturn 
      location_info:get_location - get_location(ip) results 
   :return: 
      Address based on IP, if fails return False 
   """
   output = '' 
   location_info = get_location(ip) 
   location_info_dict = __convert_json(location_info) 
   if not location_info_dict:
      print('Failed to get address from IP %s' % ip) 
      output = False 
   else: 
      if location_info_dict['city'] != '': 
         output += location_info_dict['city'] + ', ' 
      if location_info_dict['region_name'] != '' and output != '': 
         output += location_info_dict['region_name'] + ' ' 
      elif location_info_dict['region_name'] != '': 
         output += location_info_dict['region_name'] + ', '
      if output != '': 
         output += location_info_dict['country_code']
      else: 
         output += location_info_dict['country_name']

   return output 

def get_log_lat(ip:str): 
   """
   Based on an IP, execute get_location + return latitude and longitude 
   :args: 
      ip:str - IP to check 
   :param: 
      output:str - (latitude, longitude) 
      location_info:get_location - get_location(ip) results
   :return: 
      latitude and longitude
   """
   output = '(%s, %s)' 
   location_info = get_location(ip)
   location_info_dict = __convert_json(location_info)
   if not location_info_dict:
      print('Failed to get address from IP %s' % ip)
      output = False
   else: 
      output = output % (location_info_dict['latitude'], location_info_dict['longitude'])
   return output 

