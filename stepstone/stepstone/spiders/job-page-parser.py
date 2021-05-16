from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from scrapy import Spider
from scrapy import Request


class JobSpider(Spider):
    name = "stepstone"

    start_urls = [
        "https://www.stepstone.de/5/ergebnisliste.html?searchTypeFrom=detailedSearch&searchOrigin=Detailed-Search_detailed-search&newsearch=1&keyword=&freetext_exact=false&freetext_all_words=false"
    ]

    def parse(self, response):
        for job in response.css("article[data-at='job-item']"):
            job_link = job.css("a[data-at='job-item-title']::attr(href)").get()
            time = job.css("time::text").get()
            yield response.follow(job_link, callback=self.parse_job, cb_kwargs=dict(time=time))
        
        #next_page = response.css('a[data-at="pagination-next]::attr(href)').get()
        #yield response.follow(next_page, callback=self.parse)

    def parse_job(self, response, time):
        urlParts = response.url.split('--')
        self.log(f'parsing job offer: {urlParts[1]} at {time}')

        for job in response.css("div.listing-content"):
            yield {
                'id': urlParts[-1].split('-')[0],
                'title': job.css('h1.at-header-company-jobTitle::text').get(),
                'company': job.css('a.at-header-company-name::text').get(),
                'location': job.css('li.at-listing__list-icons_location::text').get(),
                'contract_type': job.css('li.at-listing__list-icons_contract-type::text').get(),
                'work_type': job.css('li.at-listing__list-icons_work-type::text').get(),
                'online_date': job.css('li.at-listing__list-icons_date span.js-ld-OnlineDate time::attr(datetime)').get(),
                'introduction': job.css('div.at-section-text-introduction-content p').get(),
                'job_description': job.css('div.at-section-text-description-content').get(),
                'profile': job.css('div.at-section-text-profile-content').get(),
                'we_offer': job.css('div.at-section-text-weoffer-content').get(),
                'contacts': job.css('div.at-section-text-contact-content').get()
            }