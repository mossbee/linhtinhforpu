from rdflib import Graph, Namespace, RDF, RDFS, OWL, XSD

# Load the OWL file
g = Graph()
g.parse("legal_onto.owl", format="xml")

# Define the namespaces
ns = Namespace("http://www.semanticweb.org/ontologies/2024/8/legal_ontology#")

# Define the SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?agency ?cardinality
WHERE {
  :Constitution rdfs:subClassOf ?restriction .
  ?restriction rdf:type owl:Restriction .
  ?restriction owl:onClass ?agency .
  ?restriction owl:onProperty :canBePromulgatedBy .
  ?restriction owl:qualifiedCardinality ?cardinality .
}
"""

# Run the query
results = g.query(query)

# Print the results
for row in results:
    print(f"Agency: {row.agency}, Cardinality: {row.cardinality}")