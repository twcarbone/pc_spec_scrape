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


def get_family_links(url, panel_label, show=False):
    """
    This function expects a soup object of the root URL of Intel processors, as
    well as a PanelLabel tag. The Panellabels correspond to each product line
    of Intel processors. The function returns a list of URLs for each model CPU
    in the given product line.
    """
    soup = get_soup(url)
    g = soup.find_all("div", {"data-parent-panel-key" : panel_label})

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


def get_model_links(url, show_links=False):
    """ """
    soup = get_soup(url)
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
        

def get_cpu_data(url, show_data=False):
    """
    Return a dictionary of CPU data from the beautiful soup object `soup`.
    """
    soup = get_soup(url)
    g = soup.find_all("ul", {"class" : "specs-list"})

    specs = {
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
    
    for key in specs.keys():
        h = soup.find_all("span", {"data-key" : key})
        try:
            h = h[0].get_text().strip()
        except:
            h = "__None__"

        specs[key] = h.replace(u"\u2122", '').replace(u"\u00AE", '')

    name = specs["ProductGroup"] + " " + specs["ProcessorNumber"]

    if show_data:
        print(name)

    return (specs, name)


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




