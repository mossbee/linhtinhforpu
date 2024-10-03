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
  :Resolution rdfs:subClassOf ?restriction .
  ?restriction owl:onClass ?unionClass ;
               owl:onProperty :PromulgatedBy ;
               ?cardinalityType ?cardinalityNum .
  ?unionClass owl:unionOf ?unionList .
  ?unionList rdf:rest*/rdf:first ?agency .
  FILTER(?cardinalityType = owl:qualifiedCardinality)
}
"""

# Execute the query
results = g.query(query)

# Process the results
agencies = []
cardinality_type = None
cardinality_value = None

for row in results:
    agencies.append(str(row.agency).split('#')[-1])
    cardinality_type = str(row.cardinalityType).split('#')[-1]
    cardinality_value = int(row.cardinalityNum)

output = [{
    "Agencies": agencies,
    "Property": "unionOf",
    "Cardinality Type": cardinality_type,
    "Cardinality Value": cardinality_value
}]

print(output)