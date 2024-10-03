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

SELECT ?agency ?relation ?cardinalityType ?cardinalityNum
WHERE {
  :JointCircular rdfs:subClassOf ?intersectionClass .
  ?intersectionClass owl:intersectionOf ?intersectionList .
  
  ?intersectionList rdf:rest*/rdf:first ?restriction .
  ?restriction owl:onClass ?unionClass ;
               owl:onProperty :PromulgatedBy ;
               ?cardinalityType ?cardinalityNum .
  ?unionClass owl:unionOf ?unionList .
  ?unionList rdf:rest*/rdf:first ?agency .
  
  BIND(IF(?cardinalityType = owl:minQualifiedCardinality, "minQualifiedCardinality", "someValuesFrom") AS ?relation)
}
"""

# Execute the query
results = g.query(query)

# Parse results into the desired format
output = []
current_relation = None
current_agencies = []
current_cardinality_type = None
current_cardinality_num = None

for row in results:
    agency = str(row.agency).split('#')[-1]
    relation = str(row.relation)
    cardinality_type = str(row.cardinalityType).split('#')[-1]
    cardinality_num = int(row.cardinalityNum) if row.cardinalityNum else None
    
    if relation != current_relation:
        if current_relation is not None:
            output.append({
                "Agencies": current_agencies,
                "Relation": current_relation,
                "Cardinality Type": current_cardinality_type,
                "Cardinality Num": current_cardinality_num
            })
        current_relation = relation
        current_agencies = [agency]
        current_cardinality_type = cardinality_type
        current_cardinality_num = cardinality_num
    else:
        current_agencies.append(agency)

# Append the last group
if current_relation is not None:
    output.append({
        "Agencies": current_agencies,
        "Relation": current_relation,
        "Cardinality Type": current_cardinality_type,
        "Cardinality Num": current_cardinality_num
    })

print(output)