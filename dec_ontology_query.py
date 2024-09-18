from owlready2 import *
from rdflib import Graph

# Load the ontology
onto = get_ontology("legal_onto.owl").load()

# Convert the ontology to an RDF graph
graph = Graph()
for triple in onto.world.as_rdflib_graph().triples((None, None, None)):
    graph.add(triple)

# Define the SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?onProperty ?onClass ?cardinality ?restrictionType
WHERE {
  # Query for the Joint_Circulars class
  ?documentClass rdf:type owl:Class ;
                 rdfs:subClassOf ?restriction ;
                 rdfs:label "Joint_Circulars" .

  # Extract restriction details
  ?restriction rdf:type owl:Restriction ;
               owl:onProperty ?onProperty ;
               owl:onClass ?onClass .

  OPTIONAL {
    # Extract cardinality restrictions
    ?restriction owl:qualifiedCardinality ?cardinality .
    BIND("qualifiedCardinality" AS ?restrictionType)
  }
  OPTIONAL {
    # Extract min cardinality restrictions
    ?restriction owl:minQualifiedCardinality ?cardinality .
    BIND("minQualifiedCardinality" AS ?restrictionType)
  }
  OPTIONAL {
    # Extract some values from restrictions
    ?restriction owl:someValuesFrom ?someClass .
    BIND("someValuesFrom" AS ?restrictionType)
  }
}
"""

# Execute the SPARQL query
results = graph.query(query)

# Print the results
for row in results:
    print(f"Restriction: {row.restriction}, On Property: {row.onProperty}, On Class: {row.onClass}, Min Qualified Cardinality: {row.minQualifiedCardinality}, Some Values From: {row.someValuesFrom}")

# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX owl: <http://www.w3.org/2002/07/owl#>

# SELECT ?restriction ?onProperty ?onClass ?minQualifiedCardinality ?someValuesFrom
# WHERE {
#   ?class rdfs:label "Joint_Circulars" .
#   ?class rdfs:subClassOf ?restriction .
#   ?restriction owl:onProperty ?onProperty .
#   OPTIONAL { ?restriction owl:onClass ?onClass . }
#   OPTIONAL { ?restriction owl:minQualifiedCardinality ?minQualifiedCardinality . }
#   OPTIONAL { ?restriction owl:someValuesFrom ?someValuesFrom . }
# }
