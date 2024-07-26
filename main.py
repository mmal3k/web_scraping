from bs4 import BeautifulSoup
import requests
import time

print("Put some skill that you are not familiar with")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}")
def find_jobs(): 
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
    html_text = requests.get(url).text
    soup  = BeautifulSoup(html_text , "lxml")
    jobs  = soup.find_all("li",class_ = "clearfix job-bx wht-shd-bx")
    for index , job in enumerate(jobs):
        published_date = job.find("span" , class_ ="sim-posted").span.text
        if "few" in published_date : 
            company = job.find("h3" , class_="joblist-comp-name").text.strip()
            skills =job.find("span", class_="srp-skills").text.replace(" ","").strip()
            more_info = job.header.h2.a["href"]
            if unfamiliar_skill not in skills : 
                with open(f"posts/{index}.txt", "w") as f:
                    f.write(f"company name : {company} \n")
                    f.write(f"skills : {skills} \n")
                    f.write(f"more_info : {more_info} \n")
                print(f"File saved :{index}")

if __name__ == "__main__":
    while True : 
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)