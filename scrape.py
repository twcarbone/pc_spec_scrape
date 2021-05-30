import requests
from bs4 import BeautifulSoup as bs


def get_soup(url):
    """
    Product Collection
    Code Name
    Vertical Segment
    Processor Number
    Status (Launched, Discontinued)
    Launch Date
    Lithography
    Use Conditions
    
    # Cores
    # Threads
    Base Frequency
    Max Turbo Frequency
    Cache
    Bus Speed
    TDP

    ~Skip~

    Max Memory Size
    Memory Types
    Max # Memory Channels
    Max Memory Bandwidth
    
    Processor Graphcs
    Graphcis Base Frequency
    Graphics Max Frequency
    Graphics Video Max Memory
    Execution Units
    4K Support
    Hax Resolution (HDMI)
    Hax Resolution (DP)
    
    PCIe Revision Supported
    PCIe Configurations
    PCIe Max # Lanes
    
    Sockets Supported
    

    """
    page = requests.get(url)
    soup = bs(page.content, "html.parser")

    g = soup.find_all("ul", {"class" : "specs-list"})

    data_keys = ("ProductGroup", "CodeNameText", "MarketSegment",
        "ProcessorNumber", "StatusCodeText", "BornOnDate", "Lithography", 
        "CertifiedUseConditions", "CoreCount", "ThreadCount", "ClockSpeed", 
        "ClockSpeedMax", "Cache", "Bus")

    spec_data = {
        "ProductGroup" : "",
        "CodeNameText" : "", 
        "MarketSegment" : "",
        "ProcessorNumber" : "",
        "StatusCodeText" : "",
        "BornOnDate" : "",
        "Lithography" : "", 
        "CertifiedUseConditions" : "",
        "CoreCount" : "",
        "ThreadCount" : "",
        "ClockSpeed" : "",
        "ClockSpeedMax" : "",
        "Cache" : "",
        "Bus" : ""}
    
    for key in spec_data.keys():
        h = soup.find_all("span", {"data-key" : key})
        h = h[0].get_text().strip()
        spec_data[key] = h

        print("%s\t%s" % (key, h))

    print(spec_data)

#    print(list(g[0].children))
    
#    for item in g:
#        print("--------------")
#        print(item.prettify())    
#    
        
