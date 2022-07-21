
from selenium import webdriver
import pandas as pd
import time 




def convert_to_csv(final_dataframe):
    final_dataframe.to_csv("final_task_final.csv",index=False)
def main():
    options = webdriver.ChromeOptions()
    options.headless = True # use headless mode screen shots for full page
    driver = webdriver.Chrome(executable_path="/home/biman/PycharmProjects/selen/chromedriver", options = options)
    dff = pd.read_csv('url.csv')
    urls = dff.values.tolist()
    urls = [item for items in urls for item in items]
    final_dataframe = pd.DataFrame()
    link_number = 1
    for url in range(len(urls)):
        driver.get(urls[url])
        elements = driver.find_elements_by_xpath("//h3/parent::a/ancestor::div[@data-hveid and @data-ved and @class='g tF2Cxc'] | //h3//parent::a/ancestor::div[@data-hveid and @data-ved]/parent::div[contains(@class,'g')][not(./ancestor::ul)]/parent::div[not(@id) or @id='rso']/div[contains(@class,'g')][not(./ancestor::ul)][not(@data-md)][not(descendant::table)][not(./g-card)][not(parent::div[contains(@class,'V3FYCf')])] | //h3//parent::a/ancestor::div[@data-hveid and @data-ved]/ancestor::div[@class='g']/parent::div[@data-hveid]//div[@data-hveid and @data-ved][not(./ancestor::ul)][not(parent::div[contains(@class,'g ')])] | //h3/parent::a/ancestor::div[contains(@class,'ZINbbc') and contains(@class,'uUPGi')]/parent::div | //a[contains(@href,'youtube')][./h3][not(ancestor::div[contains(@style,'display:none')])]/ancestor::div[not(@*)][parent::div[contains(@class,'g')]]")
        name = []
        link = []
        content = []
        for elem in elements:
            names = elem.find_elements_by_class_name("LC20lb")
            for nam in names:
                name.append(nam.text)
            links= elem.find_elements_by_class_name("TbwUpd.NJjxre")
            for lin in links:
                link.append(lin.text)
            contents = elem.find_elements_by_class_name("VwiC3b")
            for cont in contents:
                content.append(cont.text[0:100])
        #print(link)
        s1 = pd.Series(name)
        s2 = pd.Series(link)
        s3 = pd.Series(content)
        #print(s3)
        df = pd.concat([s1, s2, s3], axis=1)
        df.columns = ['title', 'link', 'content']
        #print(df)

        indexx = []
        field = []
        value = []
        j=1
        for index,content in df.iterrows():
            for i in range(len(content)):
                indexx.append(f" {link_number}.{j}.{i+1}")
            j=j+1
        j=0        
        for index,content in df.iterrows():
            for i in range(len(content)):
                field.append(content.index[i])
                value.append(content[i])
                j = j+1
        
        link_number = link_number + 1
        # series
        s1 = pd.Series(indexx) 
        s2 = pd.Series(field)
        s3 = pd.Series(value)
        final_df =pd.concat([s1, s2, s3], axis=1)
        final_df.columns = ['index','field','value']
        final_df = final_df.sort_values(by=['field','index'])
        final_dataframe = pd.concat([final_dataframe, final_df])
    #print(final_dataframe)
    convert_to_csv(final_dataframe)

if __name__=="__main__":
    main()


# In[ ]:




