import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self,url):
        self.url = url
        self.user_agent = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}
        self.response = requests.get(url = self.url, headers = self.user_agent).text
        self.soup = BeautifulSoup(self.response, 'lxml')

    def product_title(self): 
        title = self.soup.find("span" , {"id" : "productTitle"})
        if title is not None : 
            return title.text.strip()
        else :
            return "Tag Not Found"

    def product_price(self):    
        price = self.soup.find("span" , {"class" : "a-price-whole"})
        if price is not None : 
            return price.text.strip()
        else :
            return "Tag Not Found"


device = PriceTracer(url="https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CS5Z3T4M/ref=asc_df_B0CS5Z3T4M?mcid=48012694a08a39539ba003c56cdef1f0&tag=googleshopdes-21&linkCode=df0&hvadid=709962856229&hvpos=&hvnetw=g&hvrand=17772791252292532230&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061830&hvtargid=pla-2282976224153&gad_source=1&th=1")
print(device.product_price)
print(device.product_title)