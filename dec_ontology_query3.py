import rdflib

# Load the ontology
g = rdflib.Graph()
g.parse("legal_onto.owl", format="xml")

# Define the SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?agency ?cardinality
WHERE {
  :Joint_Resolutions rdfs:subClassOf ?restriction .
  ?restriction owl:onProperty :canBePromulgatedBy ;
               owl:onClass ?agencyClass ;
               owl:qualifiedCardinality ?cardinality .
  ?agencyClass owl:unionOf/rdf:rest*/rdf:first ?agency .
}
"""

# Execute the query
results = g.query(query)

# Print the results
for row in results:
    print(f"Agency: {row.agency}, Cardinality: {row.cardinality}")