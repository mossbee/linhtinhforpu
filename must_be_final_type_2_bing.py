from rdflib import Graph

# Load the ontology
g = Graph()
g.parse("legal_onto.owl")

# Define the SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?agency ?cardinalityType ?cardinalityNum
WHERE {
  :Resolution rdfs:subClassOf ?restriction .
  ?restriction owl:onProperty :PromulgatedBy ;
               owl:onClass ?unionClass ;
               owl:qualifiedCardinality ?cardinalityNum .
  ?unionClass owl:unionOf ?unionList .
  ?unionList rdf:rest*/rdf:first ?agency .
  BIND("qualified" AS ?cardinalityType)
}
"""

# Execute the query
results = g.query(query)

# Process the results
result_list = []
for row in results:
    result_list.append({
        "Agencies": [str(row.agency).split('#')[-1]],
        "Cardinality Type": str(row.cardinalityType),
        "Cardinality Num": int(row.cardinalityNum)
    })

print(result_list)
