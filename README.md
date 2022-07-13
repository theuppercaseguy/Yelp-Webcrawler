# **Yelp-Webcrawler-Scrapper**
A Yelp Web Crawler/Scrapper use to find info of anything using a given URL (optional: save it into an excell file)

Extract **Title**,**phone no**,**location** and **website** of any buisness and can be stored in an **Excell** file.

# Usage:
extracting all the data of restraunts in georgia,VT,UnitedStates.

link: [https://www.yelp.com/search?find_desc=Restaurants&find_loc=Georgia%2C+VT%2C+United+States](url)


```
$python webcrawler.py -u 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Georgia%2C+VT%2C+United+States' -p 2 -o file.xlsx

```


### output:

```

page: 1 scanned
page: 2 scanned

```
