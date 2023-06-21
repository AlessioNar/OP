from SPARQLWrapper import SPARQLWrapper, JSON, RDF, CSV

def execute_sparql_query(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(CSV)

    try:
        results = sparql.query().convert()
        return results
    except Exception as e:
        print(f"An error occurred during the SPARQL query: {str(e)}")
        return None

endpoint_url = "https://publications.europa.eu/webapi/rdf/sparql"

cellarId = "d4dcb496-b0e2-42fb-89c4-d21fada95c91.0004"

query = """
    PREFIX cdm: <https://publications.europa.eu/ontology/cdm#>

    SELECT * WHERE {
        GRAPH <http://publications.europa.eu/resource/cellar/"""+ cellarId + """> {
        ?s ?p ?o .
        }
    }
    ORDER BY ?s ?p ?o
"""

results = execute_sparql_query(endpoint_url, query)
print(results)

