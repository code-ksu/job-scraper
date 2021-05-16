# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field

class JobOffer(Item):
    title = Field()
    company = Field()
    location = Field()
    contract_type = Field()
    work_type = Field()
    online_date = Field()
    introduction = Field()
    job_description = Field()
    profile = Field()
    we_offer = Field()
    contacts = Field()