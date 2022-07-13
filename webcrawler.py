from os import system
from openpyxl import Workbook
import requests
from bs4 import  BeautifulSoup
import argparse

data= []

def yelp_spider(max_pages=0,URL=''):
   
   page = 0
   pages = []
   system('cls')
   while page <= max_pages:
      pages.append(requests.get(URL + '&start='+str(page*10)))
      print('page: ',page+1,' scanned')
      page+=1
   
   print('\n\n')
   page=0
   while page<=max_pages:
      # url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Georgia%2C+VT%2C+United+States&start=' + str(page * 10)
      
      plain_text = pages[page].text     
      soup = BeautifulSoup(plain_text,'html.parser')#gets all the links and images and sorts them in the soup object
      
      it=0      
      for link in soup.findAll('a',{'class':'css-1m051bw'}):
         title = link.string
         href = 'https://www.yelp.com' + link.get('href')
         if it < 2:##first 2 are always adds
            it+=1
            continue
         print('title: ',title)
         get_inside_data(href,title)
      
      page+=1
      print('page: ',page,' Done')
   
   
def get_inside_data(item_url,title):
   
   page_source_code = requests.get(item_url)
   plain_text = page_source_code.text 
   soup = BeautifulSoup(plain_text,'html.parser') 
   
   sibs = soup.find_all('div',attrs={'class':'css-1vhakgw border--top__09f24__exYYb border-color--default__09f24__NPAKY'})
   
   website_addr=''
   ph_no=''
   location=''
   
   for divs in sibs:
      text = str(divs.text)

      ##phone number
      if 'Phone' in text:
         ph_no = text.replace('Phone number','')
         print('phone No: ',ph_no)
         # break

      ##Shop addres
      if 'Get Directions' in text:
         location = text.replace('Get Directions','')
         print('location: ',location)
         # break      
      
      ##website address
      soup2 = BeautifulSoup(str(divs),'html.parser')
      for j in soup2.find_all('a',attrs={'class':'css-1um3nx'}):
         
         if 'biz' in str(j.get('href')):
            website_addr='https://www.yelp.com' + j.get('href')
            print('website: ',website_addr)
            break
   
   # system('cls')
   data.append([title,ph_no,location,website_addr])
   # print('list: ',data)

   print("\n#########################################\n")


if __name__ =='__main__':
   
   
   
   parser = argparse.ArgumentParser()
   
   parser.add_argument('-p',type=int,default='0',help=' is for how many pages you want to scrap,i.e: -p 2, will scan the firest 2 pages of a given link')
   
   parser.add_argument('-u',type=str,help='Enter the URL of the first page to start parsing from there.',required=True)
   
   parser.add_argument('-o',type=str ,default='file',help='used to export an excell file with a given name',required=False)
   
   args = parser.parse_args()
   
   yelp_spider(args.p - 1,args.u)
   
   if args.o:
      wb = Workbook() # creates a workbook object.
      ws = wb.active # creates a worksheet object.

      for row in data:
         ws.append(row) # adds values to cells, each list is a new row.
      wb.save(args.o) # save to excel file.