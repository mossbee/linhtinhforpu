import rdflib

# Load the RDF data into an RDFLib graph
g = rdflib.Graph()
g.parse("legal_onto.owl", format="xml")

# SPARQL query to handle the intersectionOf and unionOf collections for Joint_Resolutions
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX ns: <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?property
WHERE {
  ns:Constitution rdfs:subClassOf ?class .
  ?class owl:intersectionOf ?collection .
  ?collection rdf:rest*/rdf:first ?restriction .
  ?restriction owl:onProperty ?property .
}
"""

# Execute the query
results = g.query(query)

# Print only the local name of the property
for row in results:
    property_name = row.property.split('#')[-1]
    print(f"Property: {property_name}")
