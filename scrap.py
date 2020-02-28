# -*- coding: utf-8 -*- 
import datetime
import requests
import argparse
from lxml import html, etree

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required = False,
	help = "Your xls")
args = vars(ap.parse_args())
bus_station = args['file']

def read_file(filename):
    with open(filename, 'rb') as input_file:
        text = input_file.read()
    return text

def write_file(url):
    r = requests.get(url)
    with open('test.html', 'wb') as output_file:
        output_file.write(r.text.encode('cp1251'))

#bus_station = 'Kirovskiy z-d'
destination = 'to region'
#bus_list = ['481', '484']

def get_url_list(bus_station = "Kirovskiy z-d"):

    
    if bus_station == 'Kirovskiy z-d':
        url_list = ['https://orgp.ru/ostm/15041-05021.html', 'https://orgp.ru/ostm/15082-05021.html']
        bus_list = ['481', '484']
            
    elif bus_station == 'Gorelovo -> R-V':
        url_list = ['https://orgp.ru/ostm/15041-01081.html', 'https://orgp.ru/ostm/15082-01081.html']
        bus_list = ['481', '484']
        
    elif bus_station == 'Gorelovo -> SPb':
        url_list = ['https://orgp.ru/ostm/15041-03059.html', 'https://orgp.ru/ostm/15082-03059.html']
        bus_list = ['481', '484']

    elif bus_station == 'Ropsha':
        url_list = ['https://orgp.ru/ostm/15041-04777.html']
        bus_list = ['481']

    elif bus_station == 'R-V -> Ropsha':
        url_list = ['https://orgp.ru/ostm/15041-01561.html', 'https://orgp.ru/ostm/15082-01561.html']
        bus_list = ['481', '484']
        
    elif bus_station == 'R-V -> SPb':
        url_list = ['https://orgp.ru/ostm/15041-05754.html', 'https://orgp.ru/ostm/15082-05754.html']
        bus_list = ['481', '484']

    #пишет хрень в ответ
    else:
        url_list = ['https://orgp.ru/ostm/15041-05754.html', 'https://orgp.ru/ostm/15082-05754.html']
        bus_list = ['481', '484']
    
	
    return(url_list, bus_list)
    
#r = requests.get(url)
#with open('test.html', 'wb') as output_file:
#    output_file.write(r.text.encode('cp1251'))
  
def get_schedule(url, bus):
    write_file(url)
    text = read_file('test.html')
    tree = html.fromstring(text)
    #film_list_lxml = tree.xpath('//*[@id="out"]/div[2]/div[4]/table[2]/tbody')[0].text

    current_time = datetime.datetime.now()

    schedule=[]
    for k in range(3):
        hour = str(current_time.hour+2+k)
        minute = str(current_time.hour+2+k)
        #print(hour)
        #print('текущий час', current_time.hour)
        
        try:
            hour = tree.xpath('//*[@id="out"]/div[2]/div[5]/table[2]/tbody/tr[1]/td['+hour+']')[0].text
            minute = tree.xpath('//*[@id="out"]/div[2]/div[5]/table[2]/tbody/tr[3]/td['+minute+']')[0].text
            time = hour+':'+minute
            # print('LEN = ', len(time))
            # print('TIME = ', time)
            if len(time) == 6:
                schedule.append(time)
            elif len(time) == 9:
                time2 = time[0:5]
                schedule.append(time2)
                time3 = time[0:2] + ':' + time[6:8]
                schedule.append(time3)
            else:
                time2 = time[0:5]
                schedule.append(time2)
                time3 = time[0:2] + ':' + time[6:8]
                schedule.append(time3)
                time4 = time[0:2] + ':' + time[9:]
                schedule.append(time4)
        
        except:
            pass
        
        

    print(bus, schedule)
    return[bus, schedule]

def test():
    print('!')
    
def run(bus_station):
    response=[]
    url_list, bus_list = get_url_list(bus_station)
    #a = len(url_list)
    a = 0
    #print('a = ', a)
    for url in url_list:
        #print('a = ', a)
        r = get_schedule(url, bus_list[a])
        print('bus_list = ',bus_list[a])
        response.append(r)
        a=a+1
    
    return response

run(bus_station)
'''
17
//*[@id="out"]/div[2]/div[4]/table[2]/tbody/tr[1]/td[19]
//*[@id="out"]/div[2]/div[4]/table[2]/tbody/tr[3]/td[20]
//*[@id="out"]/div[2]/div[4]/table[2]/tbody/tr[3]/td[21]
02
//*[@id="out"]/div[2]/div[4]/table[2]/tbody/tr[3]/td[19]

//*[@id="out"]/div[2]/div[4]/table[2]/tbody
7
//*[@id="out"]/div[2]/div[4]/table[2]/tbody/tr[1]/td[9]
11
//*[@id="out"]/div[2]/div[4]/table[2]/tbody/tr[3]/td[9]
8
//*[@id="out"]/div[2]/div[4]/table[2]/tbody/tr[1]/td[10]
//*[@id="out"]/div[2]/div[4]/table[2]/tbody/tr[3]/td[10]
'''
