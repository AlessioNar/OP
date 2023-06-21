from SPARQLWrapper import SPARQLWrapper, JSON, RDF, CSV

def execute_sparql_query(endpoint_url, cellarId):
    sparql = SPARQLWrapper(endpoint_url)
    query = build_sparql_query(cellarId)
    sparql.setQuery(query)
    sparql.setReturnFormat(CSV)

    try:
        results = sparql.query().convert()
        return results
    except Exception as e:
        print(f"An error occurred during the SPARQL query: {str(e)}")
        return None

def build_sparql_query(cellarId):
    query = """
        PREFIX cdm: <https://publications.europa.eu/ontology/cdm#>

        SELECT * WHERE {
            GRAPH <http://publications.europa.eu/resource/cellar/"""+ cellarId + """> {
            ?s ?p ?o .
            }
        }
        ORDER BY ?s ?p ?o
    """
    return query
