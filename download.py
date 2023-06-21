# Function that from a csv file, makes a get request to the url, and saves the response to a file. 

import csv
import requests
import os

base_url = "http://publications.europa.eu/resource/celex/"

# url should be composed of the base url and the celex number
def download_rdf_from_url(url, file_path):
    response = requests.get(url, headers={"Accept": "application/rdf+xml", "Accept-Language": "eng"})
    with open(file_path, "wb") as f:
        f.write(response.content)
    return None

def download_rdf_from_csv(csv_file_path):
    with open(csv_file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = base_url + row["celex"]            
            file_path = 'data/rdf/'+ row["celex"] + '.rdf'
            # check if file exists with 
            if os.path.isfile(file_path):
                pass
            else:
                download_rdf_from_url(url, file_path)
    return None



def download_full_tree(cellarId, file, what="tree"):
    # Remove what is after the . in the cellarId
    cellarId = cellarId.split(".")[0]
    if what == "tree":
        url = "https://publications.europa.eu/resource/cellar/" + cellarId + "/rdf/tree/full"
        response = requests.get(url)
        with open("data/tree/" + file, "wb") as f:
            f.write(response.content)
    elif what == "object":
        url = "https://publications.europa.eu/resource/cellar/" + cellarId + "/rdf/object/full"    
        response = requests.get(url)
        with open("data/object/" + file, "wb") as f:
            f.write(response.content)
    return None
