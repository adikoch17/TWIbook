import time
from selenium import webdriver

url = 'https://wanderinginn.com/2018/07/10/5-00/'


browser = webdriver.Chrome()
browser.get(url)    

chaptersLeft = True
fl = open("./thebook/twi5.txt", "a")

while chaptersLeft:
    url = browser.current_url
    fname=url.split('/')
    fl.write(fname[-2]+"\n\n\n\n\n\n")
    paragraphs = browser.find_elements_by_css_selector(".entry-content>p")
    for i in paragraphs:
        try:
            fl.write(i.text+ "\n")
        except:
            fl.write("ERROR HERE")
            continue
    try:
        nextButton = browser.find_element_by_css_selector(".entry-content>p:last-child>span")
    except:
        try:
            nextButton = browser.find_element_by_css_selector(".entry-content>p:last-child>a:last-child>span")
        except:
            nextButton = browser.find_element_by_css_selector(".entry-content>div:last-child>p>span")
    time.sleep(1)
    nextButton.click()
    time.sleep(1)
    if url == "https://wanderinginn.com/2019/03/02/interlude-5/":
        chaptersLeft = False
        print("chapters over")
    else:
        fl.write("\n\n\n\n\n\n")
        print("chapter done")






