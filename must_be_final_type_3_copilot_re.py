from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

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

SELECT ?agencies ?property ?cardinalityType ?cardinalityValue
WHERE {
  :JointResolution rdfs:subClassOf ?restriction .
  ?restriction owl:onProperty :PromulgatedBy ;
               owl:someValuesFrom ?unionClass .
  ?unionClass owl:unionOf ?unionList .
  ?unionList rdf:rest*/rdf:first ?intersectionList .
  ?intersectionList owl:intersectionOf ?agencies .
  OPTIONAL { ?restriction owl:cardinality ?cardinalityValue }
  BIND("intersectionOf" AS ?property)
  BIND("someValuesFrom" AS ?cardinalityType)
}
"""

# Run the query
qres = g.query(query)

# Process the results
results = []
for row in qres:
    agencies = [str(agency) for agency in row.agencies]
    result = {
        "Agencies": agencies,
        "Property": row.property,
        "Cardinality Type": row.cardinalityType,
        "Cardinality Value": row.cardinalityValue if row.cardinalityValue else None,
    }
    results.append(result)

print(results)