import time
import json

import scrape as scrape

start_time = time.time()

ROOT_URL = "https://ark.intel.com/content/www/us/en/ark.html"

# The root URL of the intel processor specification page includes clickable
# 'panels' to each major product line (e.g., 'Core', 'Xeon', 'Celeron', etc.)
product_lines = {
    'Core' : 'PanelLabel122139',
    'Celeron' : 'PanelLabel43521',
    'XeonPhi' : 'PanelLabel75557',
    'Atom' : 'PanelLabel29035',
    'Pentium' : 'PanelLabel29826',
    'Xeon' : 'PanelLabel595',
    'Itanium' : 'PanelLabel451',
    'Quark' : 'PanelLabel79047'
    }

# Each product line (e.g., 'Core') contains multiple families of CPU (e.g.,
# 11th Generation Core i9, 7th Generation Core i7, 10th Generation Core i3).
# Here, we get a list of all URLs, each one corresponding to a family of
# processors.
family_urls = scrape.get_family_links(ROOT_URL, product_lines['Core'])

cpu_specs = {}
for i, family_url in enumerate(family_urls):

    # Here, we get a list of all of the URLs for each CPU model within each
    # product family. For example, within the product family '9th Generation
    # Core i7' there are models 'Core i7-9700K', 'Core i7-9750H', 'Core
    # i7-9850HE', etc. 
    model_urls = scrape.get_model_links(family_url)

    for j, model_url in enumerate(model_urls):

        # Return a name and dictionary to each CPU
        (cpu_data, name) = scrape.get_cpu_data(model_url, True)

        cpu_specs[name] = cpu_data

#       scrape.insert_into_db(cpu_data)
#       print("Done %d/%d families. Done %d/%d models." %
#             (i, len(family_urls)-1, j, len(model_urls)-1))

    break

# Print the output of the script to a JSON file
with open("./outfiles/Intel.json", "w") as outfile:
    json.dump(cpu_specs, outfile)

print("Finished in %d seconds." % (time.time() - start_time))
