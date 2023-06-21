# This script is the main script for the project. It will be used to run the
# other scripts.


import extract
import sparql
import download
import os

# Use the cellarId to make a SPARQL query
# Save the results of the SPARQL query to a csv file
if __name__ == "__main__":
    # Download the rdf files from the csv file
    download.download_rdf_from_csv("data/RCL.csv")
    print("Downloaded all rdf files")
    # Loop through the .rdf files in the data folder
    for file in os.listdir("data/rdf"):
        # For each file, extract the cellarId        
        cellarId = extract.extract_rdf_about_from_file("data/rdf/" + file)
        # Use the cellarId to make a SPARQL query
        results = sparql.execute_sparql_query("https://publications.europa.eu/webapi/rdf/sparql", cellarId)
        # Save the results of the SPARQL query to a csv file
        with open("data/csv/" + file + ".csv", "w") as f:
            f.write(results.decode("utf-8"))
        print("Saved " + file + " to csv")
    
