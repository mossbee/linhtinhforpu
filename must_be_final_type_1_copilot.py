from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, OWL, XSD

# Load the ontology
g = Graph()
g.parse("legal_onto.owl")

# Define namespaces
ns = Namespace("http://www.semanticweb.org/ontologies/2024/8/legal_ontology#")

# SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?agency ?cardinalityType ?cardinalityNum
WHERE {
  :Constitution rdfs:subClassOf ?restriction .
  ?restriction owl:onClass ?agency ;
               owl:onProperty :PromulgatedBy ;
               ?cardinalityType ?cardinalityNum .
  FILTER(?cardinalityType = owl:qualifiedCardinality)
}
"""

# Execute the query
results = g.query(query)

# Parse results into the desired format
output = []
for row in results:
    output.append({
        "Agencies": [str(row.agency).split('#')[-1]],
        "Cardinality Type": "qualified",
        "Cardinality Num": int(row.cardinalityNum)
    })

print(output)