# web-scraping
### Note: This is a follow along project

The tutorial that I'm following, [click here](https://youtu.be/Pu3gmdWsLYc)
<br>
Currently the code is facing a server error due to the changes made to the website's codebase as compared to the version used in the video. ( The website used in this video - [click here](https://directory.ntschools.net/#/schools) )

### Error screenshot

![image](https://github.com/CJ445/web-scraping/assets/131938772/1467e53f-7e29-4fbf-af64-eaa7a6b9aad6)

I will be attempting to fix it by learning more about scrapy.

### commands to set up

- download project
```
git clone https://github.com/CJ445/web-scraping.git
cd web-scraping
code .
```
- to run project, open project directory on command prompt and run this:
```
scrapy runspider ntschools.py -o all_schools.csv
```

