import csv
import requests
import time
from bs4 import BeautifulSoup

def linkedin_scraper(webpage, page_number):
    start = time.time()
    file = open('data/job_data.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'location', 'link'])

    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')

    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_='job-search-card__location').text.strip()
        job_link = job.find('a', class_='base-card__full-link')['href']
 
        writer.writerow([
        job_title.encode('utf-8'),
        job_company.encode('utf-8'),
        job_location.encode('utf-8'),
        job_link.encode('utf-8')
        ])
 
    print('Data updated')

    if page_number < 50:
        page_number = page_number + 1
        linkedin_scraper(webpage, page_number)
    else:
        file.close()
        print('File closed')
    print('Time taken:', time.time()-start, 'seconds')
# page_number=0
# webpage='https://www.linkedin.com/jobs/search/?currentJobId=3876184250&geoId=102713980&keywords=data%20analyst&location=India&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true'
# linkedin_scraper(webpage, page_number)
