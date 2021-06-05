import scrape as scrape

urls = (
    "https://ark.intel.com/content/www/us/en/ark/products/212252/intel-core-i9-11900-processor-16m-cache-up-to-5-20-ghz.html",
    "https://ark.intel.com/content/www/us/en/ark/products/series/202984/11th-generation-intel-core-i9-processors.html")

#soup_11900 = scrape.get_soup(urls[0])
#data_11900 = scrape.get_spu_data(soup_11900)

soup_11gen = scrape.get_soup(urls[1], False)
links_11gen = scrape.get_11gen_links(soup_11gen, False)

for link in links_11gen:
    soup = scrape.get_soup(link, False)
    data = scrape.get_cpu_data(soup, True)
    print("------------------------------------------------------------")

