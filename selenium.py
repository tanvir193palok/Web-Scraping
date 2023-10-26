# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# import pandas as pd

# url = "https://www.washingtonpost.com/climate-environment/environment/"
# driver = webdriver.Chrome()
# driver.get(url)

# page_num = 0
# data = {'Title': [], 'Link': []}

# while True:
#     load_more_button = driver.find_elements(By.CSS_SELECTOR, '.inline-flex.items-center.justify-center.lh-md.overflow-hidden.border-box.min-w-btn.transition-colors.duration-200.ease-in-out.font-sans-serif.font-bold.antialiased.bg-offblack.hover-bg-gray-darker.focus-bg-gray-darker.white.b-solid.bw.bc-transparent.focus-bc-black.brad-lg.pl-md.pr-md.h-md.pt-0.pb-0.w-100.pointer')

#     if load_more_button:
#         # Move to the element before clicking
#         action = ActionChains(driver)
#         action.move_to_element(load_more_button[0]).click().perform()
        
#         page_num += 1
#         print("Getting page number " + str(page_num))
#         time.sleep(1)
#     else:
#         break

# html = driver.page_source.encode('utf-8')
# driver.quit()


# soup = BeautifulSoup(html, 'html.parser')
# target= soup.find(class_ ="flex-grid flex flex-wrap mr-auto ml-auto print-mt-none")
# mains= target.find_all(class_="story-headline pr-sm")

# for main in mains:
#     a_tag = main.find('a', class_='flex hover-blue')

#     if a_tag:
#         title = a_tag.find('h3').text
#         link = a_tag['href']
#         data['Title'].append(title)
#         data['Link'].append(link)

# # Create a DataFrame from the dictionary
# df = pd.DataFrame(data)

# # Save the DataFrame to an Excel file
# df.to_excel('output.xlsx', index=False)

# print("Data saved to output.xlsx")


# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# import pandas as pd

# url = "https://www.washingtonpost.com/climate-environment/environment/"
# driver = webdriver.Chrome()
# driver.get(url)

# page_num = 0
# data = {'Title': [], 'Link': []}

# while True:
#     load_more_button = driver.find_elements(By.CSS_SELECTOR, '.inline-flex.items-center.justify-center.lh-md.overflow-hidden.border-box.min-w-btn.transition-colors.duration-200.ease-in-out.font-sans-serif.font-bold.antialiased.bg-offblack.hover-bg-gray-darker.focus-bg-gray-darker.white.b-solid.bw.bc-transparent.focus-bc-black.brad-lg.pl-md.pr-md.h-md.pt-0.pb-0.w-100.pointer')

#     if load_more_button:
#         # Move to the element before clicking
#         action = ActionChains(driver)
#         action.move_to_element(load_more_button[0]).click().perform()

#         # Wait for the content to load (you might need to adjust the wait time)
#         time.sleep(2)

#         html = driver.page_source
#         soup = BeautifulSoup(html, 'html.parser')

#         target = soup.find(class_="flex-grid flex flex-wrap mr-auto ml-auto print-mt-none")
#         mains = target.find_all(class_="story-headline pr-sm")

#         for main in mains:
#             a_tag = main.find('a', class_='flex hover-blue')

#             if a_tag:
#                 title = a_tag.find('h3').text
#                 link = a_tag['href']
#                 data['Title'].append(title)
#                 data['Link'].append(link)

#         page_num += 1
#         print("Getting data from page number " + str(page_num))
#     else:
#         print("No more 'Load more' button found. Exiting.")
#         break

# # Create a DataFrame from the dictionary
# df = pd.DataFrame(data)

# # Save the DataFrame to an Excel file
# df.to_excel('output1.xlsx', index=False)

# print("Data saved to output.xlsx")


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

url = "https://www.washingtonpost.com/search/?query=Bangladesh"
driver = webdriver.Chrome()
driver.get(url)

page_num = 0
data = {'Title': [], 'Link': []}
processed_urls = set()

while True:
    # load_more_button = driver.find_elements(By.CSS_SELECTOR, '.inline-flex.items-center.justify-center.lh-md.overflow-hidden.border-box.min-w-btn.transition-colors.duration-200.ease-in-out.font-sans-serif.font-bold.antialiased.bg-offblack.hover-bg-gray-darker.focus-bg-gray-darker.white.b-solid.bw.bc-transparent.focus-bc-black.brad-lg.pl-md.pr-md.h-md.pt-0.pb-0.w-100.pointer')
    load_more_button = driver.find_elements(By.CSS_SELECTOR, '.wpds-c-kSOqLF wpds-c-kSOqLF-bywHgD-variant-primary wpds-c-kSOqLF-eHdizY-density-default wpds-c-kSOqLF-ejCoEP-icon-left')

    if load_more_button:
        # Move to the element before clicking
        action = ActionChains(driver)
        action.move_to_element(load_more_button[0]).click().perform()

        # Wait for the content to load (you might need to adjust the wait time)
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        target = soup.find(class_="flex-grid flex flex-wrap mr-auto ml-auto print-mt-none")
        mains = target.find_all(class_="story-headline pr-sm")

        for main in mains:
            a_tag = main.find('a', class_='flex hover-blue')

            if a_tag:
                title = a_tag.find('h3').text
                link = a_tag['href']

                # Check if the link is already processed
                if link not in processed_urls:
                    data['Title'].append(title)
                    data['Link'].append(link)
                    processed_urls.add(link)

        page_num += 1
        print("Getting data from page number " + str(page_num))
    else:
        print("No more 'Load more' button found. Exiting.")
        break

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('output3.xlsx', index=False)

print("Data saved to output1.xlsx")
