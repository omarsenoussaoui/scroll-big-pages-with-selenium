from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.instagram.com/sale_sucre_mascara29/')
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                  "var lenOfPage=document.body.scrollHeight;"
                                  "return lenOfPage;")
print("1 = ",lenOfPage)
match=False
x=2
while(match==False):
    lastCount = lenOfPage
    time.sleep(5)
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
        "var lenOfPage=document.body.scrollHeight;"
        "return lenOfPage;")
    print(x,"=",lenOfPage)
    print(lenOfPage-lastCount)
    x=x+1
    if lastCount==lenOfPage:
        print("lastCount = lenofpage = ",lastCount)
        match=True
