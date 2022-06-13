from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import time
from selenium.webdriver.chrome.options import Options
import warnings
from Screenshot import Screenshot_Clipping
# urls = ["https://www.google.com/search?q=shoes","https://www.google.com/search?q=shoes","https://www.google.com/search?q=shoes","https://www.google.com/search?q=jacket"]
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
# single screenshot
# sleep(1)
# driver.get_screenshot_as_file("screenshot.png")
dff = pd.read_csv('url.csv')
urls = dff.values.tolist()
urls = [item for items in urls for item in items]
# print(urls)

for url in range(len(urls)):
    driver.get(urls[url])




    def extraxt():
        link_number = 1
        final_dataframe = pd.DataFrame()
        for ur in urls:
            # print(ur)
            driver.get(ur)
            elements = driver.find_elements_by_xpath(
                "//h3/parent::a/ancestor::div[@data-hveid and @data-ved and @class='g tF2Cxc'] | //h3//parent::a/ancestor::div[@data-hveid and @data-ved]/parent::div[contains(@class,'g')][not(./ancestor::ul)]/parent::div[not(@id) or @id='rso']/div[contains(@class,'g')][not(./ancestor::ul)][not(@data-md)][not(descendant::table)][not(./g-card)][not(parent::div[contains(@class,'V3FYCf')])] | //h3//parent::a/ancestor::div[@data-hveid and @data-ved]/ancestor::div[@class='g']/parent::div[@data-hveid]//div[@data-hveid and @data-ved][not(./ancestor::ul)][not(parent::div[contains(@class,'g ')])] | //h3/parent::a/ancestor::div[contains(@class,'ZINbbc') and contains(@class,'uUPGi')]/parent::div | //a[contains(@href,'youtube')][./h3][not(ancestor::div[contains(@style,'display:none')])]/ancestor::div[not(@*)][parent::div[contains(@class,'g')]]")
            name = []
            link = []
            content = []
            for elem in elements:
                names = elem.find_elements_by_class_name("LC20lb")

                for nam in names:
                    name.append(nam.text)

                links = elem.find_elements_by_class_name("TbwUpd.NJjxre")
                for lin in links:
                    link.append(lin.text)

                contents = elem.find_elements_by_class_name("VwiC3b")
                for cont in contents:
                    content.append(cont.text[0:100])

                    # print(link)
            s1 = pd.Series(name)
            s2 = pd.Series(link)
            s3 = pd.Series(content)
            # print(s3)
            df = pd.concat([s1, s2, s3], axis=1)
            df.columns = ['Title', 'link', 'details']
            # print(df)

            indexx = []
            field = []
            value = []
            j = 1
            for index, content in df.iterrows():
                for i in range(len(content)):
                    indexx.append(f" {link_number}.{j}.{i + 1}")
                j = j + 1

            j = 0
            for index, content in df.iterrows():
                for i in range(len(content)):
                    field.append(content.index[i])
                    value.append(content[i])
                    j = j + 1
            # series

            link_number = link_number + 1
            s1 = pd.Series(indexx)
            s2 = pd.Series(field)
            s3 = pd.Series(value)
            final_df = pd.concat([s1, s2, s3], axis=1)
            final_df.columns = ['index', 'field', 'value']
            final_df = final_df.sort_values(by=['field', 'index'])
            final_dataframe = pd.concat([final_dataframe, final_df])
        print(final_dataframe)
        final_dataframe.to_csv("task_2_final.csv", index=False)


    def screenshot():
        # for url in range(len(urls)):
        #     driver.get(urls[url])
            viewport_height = driver.execute_script("return window.innerHeight")
            viewport_height -= 80  # -> to obtain full data screenshot
            height = driver.execute_script("return document.body.scrollHeight")
            i = 1  # -> for file name
            y = 0  # -> for equating height left to scroll
            while y < height:
                driver.get_screenshot_as_file("{u}_v{i}.png".format(u=url + 1, i=i))
                name = "1_v" + str(i) + ".png"
                driver.get_screenshot_as_file('./name')
                driver.execute_script(f"window.scrollBy(0,{viewport_height})")
                sleep(2)
                y += viewport_height
                i += 1


    def dump():
        i = 0
        for url in urls:
            driver.get(url)
            # driver.get(url)
            pageSource = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
            file = open("pages_source_%i.html" % i, "w")
            file.write(pageSource)
            i = i + 1
            file.close()

            # f.close()

    def fullscreen():
        i=1
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
        driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
        driver.find_element(by=By.TAG_NAME, value='body').screenshot(f'./{i}.png')
        i = i + 1

extraxt()

screenshot()
fullscreen()
dump()
