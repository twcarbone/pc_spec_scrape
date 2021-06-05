import scrape as scrape

intel_core_root = "https://ark.intel.com/content/www/us/en/ark.html#@PanelLabel122139"
intel_11geni9_root = "https://ark.intel.com/content/www/us/en/ark/products/series/202984/11th-generation-intel-core-i9-processors.html"



soup_core_root = scrape.get_soup(intel_core_root, False)
links_core_root = scrape.get_model_links(soup_core_root, True)




"""
soup_11geni9 = scrape.get_soup(intel_11geni9_root, False)
links_11geni9 = scrape.get_11gen_links(soup_11geni9, False)

for link in links_11geni9:
    soup = scrape.get_soup(link, False)
    data = scrape.get_cpu_data(soup, True)
    print("------------------------------------------------------------")
"""
