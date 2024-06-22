import scrapy
import json


class NtschoolsSpider(scrapy.Spider):
    name = "ntschools"
    start_urls = ["https://directory.ntschools.net/#/schools"]

    headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "directory.ntschools.net",
    "Pragma": "no-cache",
    "Referer": "https://directory.ntschools.net/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Gpc": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Requested-With": "Fetch"
    }
    def parse(self, response):
        url = "https://directory.ntschools.net/api/System/GetAllSchools"

        request = scrapy.Request(url,
                                callback=self.parse_api,
                                headers=self.headers)
        yield request

    def parse_api(self, response):
        base_url = "https://directory.ntschools.net/api/System/GetSchool?itSchoolCode=acacisch"
        raw_data = response.body
        data = json.loads(raw_data)

        for school in data:
            school_code = school['itSchoolCode']
            school_url = base_url+school_code
            request = scrapy.Request(
                school_url,
                callback=self.parse_school,
                headers=self.headers)
            yield request

    def parse_school(self, respone):
        raw_data = response.body
        data = json.loads(raw_data)
        yield {
            'Name' : data['name'],
            'PhysicalAddress' : data['physicalAddress']['displayAddress'],
            'PostalAddress' : data['postalAddress']['displayAddress'],
            'Email' : data['mail'],
            'Phone' : data['telephoneNumber']
        }