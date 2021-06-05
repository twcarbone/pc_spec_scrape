"""



"""
import scrape as scrape


# get list of URLs for each family of Intel Core procesors
# e.g.  11th-gen i9, 10th-gen i5, 9th-gen i7
root_url = "https://ark.intel.com/content/www/us/en/ark.html#@PanelLabel122139"
root_soup = scrape.get_soup(root_url, False)
family_urls = scrape.get_family_links(root_soup, False)

for i, family_url in enumerate(family_urls):

    # get list of URLs for each model of Intel processor in the family
    # e.g. i9-11900, i9-11900K, i9-11980HK
    family_soup = scrape.get_soup(family_url, False)
    model_urls = scrape.get_model_links(family_soup, False)

    for j, model_url in enumerate(model_urls):

        # get cpu data from each model of Intel processor
        model_soup = scrape.get_soup(model_url, False)
        cpu_data = scrape.get_cpu_data(model_soup, False)

        print("Done %d/%d familes. Done %d/%d models." %
             (i, len(family_urls), j, len(model_urls)))



