from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from scrapy import Spider
from scrapy import Request

#URL = "https://www.stepstone.de/stellenangebote--Sachbearbeiter-m-w-d-Debitoren-Duesseldorf-Services-by-Handelsblatt-Media-Group-GmbH--7059501-inline.html?suid=98ec0d4a-3eb3-4931-be66-69ad2edd91d3&rltr=3_3_25_dynrl_m_0_0_0_0_1"
#
# def parse_item(self, response):
#     item = DemoItem()
#     item["product_title"] = response.xpath("a/text()").extract()
#     item["product_link"] = response.xpath("a/@href").extract()
#     response.xpath("div[@class = 'desc']/text()").extract()
#     return items

class JobSpider(Spider):
    name = "stepstone"

    def start_requests(self):
        urls = [
            "https://www.stepstone.de/stellenangebote--Sachbearbeiter-m-w-d-Debitoren-Duesseldorf-Services-by-Handelsblatt-Media-Group-GmbH--7059501-inline.html"
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log(f'READ JOB OFFER')

        for job in response.css("div.listing-content"):
            yield {
                'title': job.css('h1.at-header-company-jobTitle::text').get(),
                'company': job.css('a.at-header-company-name::text').get(),
                'location': job.css('li.at-listing__list-icons_location::text').get(),
                'contract_type': job.css('li.at-listing__list-icons_contract-type::text').get(),
                'work_type': job.css('li.at-listing__list-icons_work-type::text').get(),
                'online_date': job.css('li.at-listing__list-icons_date::text').get(),
                'introduction': job.css('div.at-section-text-introduction::text').get(),
                'job_description': job.css('div.at-section-text-description-content::text').get(),
                'profile': job.css('div.at-section-text-profile-content::text').get(),
                'we_offer': job.css('div.at-section-text-weoffer-content::text').get(),
                'contacts': job.css('div.at-section-text-contact-content::text').get()
            }