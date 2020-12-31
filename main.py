from selenium import webdriver
import time
import urllib.request
driver=webdriver.Chrome()
driver.get('https://www.instagram.com/judo_top_video_/')
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                  "var lenOfPage=document.body.scrollHeight;"
                                  "return lenOfPage;")
#print("1 = ",lenOfPage)
match=False
x=2
while(match==False):
    lastCount = lenOfPage
    time.sleep(5)
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
        "var lenOfPage=document.body.scrollHeight;"
        "return lenOfPage;")
    #print(x,"=",lenOfPage)
    #print(lenOfPage-lastCount)
    #x=x+1
    if lastCount==lenOfPage:
     #   print("lastCount = lenofpage = ",lastCount)
        match=True

posts=[]
post_link = driver.find_elements_by_tag_name('a')
# this block get the links of the postes
for link in post_link:
    post = link.get_attribute('href')
    if '/p/' in post: #/p/====> c-a-d poste all posts in insta contain this /p/
        posts.append( post )
#print(posts)

download_url=''
for post in posts:
    driver.get(post)
    short_code=driver.current_url.split("/")[-2] #get the url of this current page
     #get the code after /p/ like CIeIUm5hiBU in https://www.instagram.com/p/CIeIUm5hiBU/
    type = driver.find_element_by_xpath('//meta[@property="og:type"]').get_attribute('content')
    if type== 'video':
        download_url=driver.find_element_by_xpath('//meta[@property="og:video"]').get_attribute('content')
        urllib.request.urlretrieve(download_url,'{}.mp4'.format(short_code))
    else:
        download_url=driver.find_element_by_xpath('//meta[@property="og:image"]').get_attribute('content')
        urllib.request.urlretrieve(download_url, '{}.jpg'.format(short_code))
    print(download_url)
