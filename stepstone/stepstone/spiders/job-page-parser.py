from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from scrapy import Spider
from scrapy import Request


class JobSpider(Spider):
    name = "stepstone"

    start_urls = [
        "https://www.stepstone.de/stellenangebote--Sachbearbeiter-m-w-d-Debitoren-Duesseldorf-Services-by-Handelsblatt-Media-Group-GmbH--7059501-inline.html",
        "https://www.stepstone.de/stellenangebote--Data-Scientist-m-w-d-Berlin-Berylls--7158683-inline.html?suid=df1f70f3-e148-4577-8df7-000e19726e6e&rltr=3_3_25_dynrl_m_0_0_0_0_1"
    ]

    def parse(self, response):
        self.log(f'READ JOB OFFER')

        for job in response.css("div.listing-content"):
            yield {
                'id': response.url.split('--')[-1].split('-')[0],
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