from .model import BaseScraper, ScraperResponse
import httpx

class ZyteScraper(BaseScraper):
    """
    Scraper that uses Zyte Extract API
    """
    default_api_url = "https://api.zyte.com/v1/extract"
    
    def prepare_request(self, url, options = None) -> httpx.Request:
        return httpx.Request(
            "POST", 
            self.api_url,
            json={
                "url": url,  
                "browserHtml": True,
            }
        )
        
    def get_request_auth(self):
        return (self.api_key, "")
        
    def parse_response(self, url, resp):
        content = resp.json()['browserHtml']
        
        return ScraperResponse(
            content=content,
            final_url=url,
            status_code=resp.status_code,
        )
