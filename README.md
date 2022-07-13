# **Yelp-Web-crawler/Scrapper**
A Yelp Web Crawler/Scrapper use to find information about any busines in any location. And also able to store it an an excell file.

Extract **Title**, **phone no**, **location** and **website** of any buisness and can be stored in an **Excell** file.


## Installation:

```
$ git clone https://github.com/theuppercaseguy/Yelp-Webcrawler.git
$ cd Yelp-Webcrawler 
$ pip install -r requirements.txt
```

Now its Ready to use....


## Usage:
```
usage: webcrawler.py [-h] [-p P] -u U [-o O]

options:
  -h, --help  show this help message and exit.
  -u U        (Required): Enter the URL of the searched Buisnessess to start parsing.
  -p P        (Optional): Is for how many pages you want to scrap (Default: 1),i.e: -p 2, will scan the firest 2 pages of a given link.
  -o O        (Optional): Used to export the collected data to excell file.
```


## Example:
Extracting data of all the **Restraunts** in **georgia,VT,UnitedStates**.

Link: [https://www.yelp.com/search?find_desc=Restaurants&find_loc=Georgia%2C+VT%2C+United+States](url)


```
$python webcrawler.py -u 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Georgia%2C+VT%2C+United+States' -p 2 -o file.xlsx

```


### OutPut:

```

page: 1 scanned
page: 2 scanned

title:  The Drake Bar and Kitchen
website:  https://www.yelp.com/biz_redir?url=http%3A%2F%2Fwww.thedrakevt.com&cachebuster=1657703153&website_link_type=website&src_bizid=RITffuaN_SH99q6Q_R49CA&s=3b96959fc7dfa356db851e7e5f97d7c3d73945cd1828e2f33e9529048566860d
phone No:  (802) 528-5991
location:  30 S Main St Saint Albans City, VT 05478

#########################################

title:  Mill River Brewing BBQ & Smokehouse
website:  https://www.yelp.com/biz_redir?url=https%3A%2F%2Fwww.millriverbrewing.com&cachebuster=1657703156&website_link_type=website&src_bizid=m-Aa-SWhu_Zfos4MdC7iEA&s=4c2f3383f8c0dbdb645eef2697865f21fc7161dd669d36561c8924b25fee49ac
phone No:  (802) 582-4182
location:  10 Beauregard Dr Saint Albans, VT 05478

#########################################

title:  Blue Paddle Bistro
website:  https://www.yelp.com/biz_redir?url=http%3A%2F%2Fwww.bluepaddlebistro.com&cachebuster=1657703160&website_link_type=website&src_bizid=iDe2fOkqdnoOdFETE1Zw8g&s=14d5b8e001736d896f6c03bb4950ac434f15521a0cc72af231fb42f476007b7e
phone No:  (802) 372-4814
location:  316 US Rt 2 South Hero, VT 05486

#########################################

title:  Arrowhead Lodge
website:  https://www.yelp.com/biz_redir?url=https%3A%2F%2Fwww.arrowheadlodgevt.com&cachebuster=1657703172&website_link_type=website&src_bizid=Dy7m1xP-XOcmc3sP2-O_TA&s=f3506361506345c455c98cb3a2ec2ac5de3246e8dcc1ff264173427375d8fa5a
phone No:  (802) 881-5882
location:  2 Main St Milton, VT 05468

#########################################

page:  1  Done
title:  Restraunts

#########################################

title:  Shore Acres Inn & Restaurant
website:  https://www.yelp.com/biz_redir?url=http%3A%2F%2Fwww.shoreacres.com&cachebuster=1657703261&website_link_type=website&src_bizid=iWYkd6fQrNCcjPPPGLUJ7g&s=382b150c9d3e0e55b967af24e7016453e661c6bb17bc00ab13dd697b9fcbf35e
phone No:  (802) 372-8722
location:  237 Shore Acres Dr North Hero, VT 05474

#########################################

title:  The Grill on Centre
phone No:  (802) 893-7425
location:  25 Centre Dr Milton, VT 05468

#########################################

title:  Bayside Pavilion
website:  https://www.yelp.com/biz_redir?url=https%3A%2F%2Fwww.stalbansbaymarina.com%2Fbayside-pavilion%2F&cachebuster=1657703287&website_link_type=website&src_bizid=VQXCtGSsfUHtrzj7_VNQmA&s=de914f740c8c448d2d0cd5c1d284573ab70601280b2adeb27522e1e9575d15c3phone No:  (802) 524-0909
location:  15 Georgia Shore Rd Saint Albans, VT 05478

#########################################

page:  2  Done

Outptput produced as: file.xlsx


by: The UPPERCASE GUY


```

### Requirements.txt
```
beautifulsoup4==4.11.1
openpyxl==3.0.10
requests==2.28.1
```


















