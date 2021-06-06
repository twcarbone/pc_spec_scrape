import requests
from bs4 import BeautifulSoup as bs
import psycopg2


def get_soup(url, show_html=False):
    """
    Return a beautiful soup object of the html from `url`.
    """
    page = requests.get(url)
    soup = bs(page.content, "html.parser")

    if show_html:
        print(soup.prettify())

    return soup


def get_family_links(soup, show=False):
    """
    PanelLabel122139    Intel Core
    PanelLabel129862    Intel Pentium
    PanelLabel143521
    PanelLabel1595
    PanelLabel175557
    PanelLabel1433521   Intel Celeron
    PanelLabel129035
    PanelLabel179047
    """
    g = soup.find_all("div", {"data-parent-panel-key" : "PanelLabel122139"})

    domain = "https://ark.intel.com"
   
    links = [] 
    for item in g:
        filepaths = item.find_all("a")
        
        links = []
        for item in filepaths:
            filepath = item.get("href")
            link = domain + filepath

            links.append(link)

            if show:
                print(link)

    return links


def get_model_links(soup, show_links=False):
    """ """
    g = soup.find_all("td", {"data-component" : "arkproductlink"})

    domain = "https://ark.intel.com"
   
    links = [] 
    for item in g:
        filepath = item.find('a')['href']
        link = domain + filepath
        
        links.append(link)

        if show_links:
            print(link)

    return links
        

def get_cpu_data(soup, show_data=False):
    """
    Return a dictionary of CPU data from the beautiful soup object `soup`.
    """

    g = soup.find_all("ul", {"class" : "specs-list"})

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
        try:
            h = h[0].get_text().strip()
        except:
            h = "__None__"
        spec_data[key] = h

        if show_data:
            print("%23s  %s" % (key, h))

    return spec_data


def insert_into_db(cpu_data):
    
    conn = psycopg2.connect("dbname=pc_hardware user=tcarbone")
    cur = conn.cursor()

    try:
        cur.execute("""
                    INSERT INTO intel_core 
                    (processor_number, core_count, thread_count, clock_speed, clock_speed_max) 
                    VALUES (%s, %s, %s, %s, %s);
                    """,
                    (cpu_data["ProcessorNumber"],
                     int(cpu_data["CoreCount"]), 
                     int(cpu_data["ThreadCount"]),
                     cpu_data["ClockSpeed"],
                     cpu_data["ClockSpeedMax"]))
        conn.commit()
    
    except Exception as err:
        raise err
        print("Failed to insert into database.")

    finally:
        cur.close()
        conn.close()




