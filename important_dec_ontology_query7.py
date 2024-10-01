from rdflib import Graph

# Load the ontology file into an RDF graph
g = Graph()
g.parse("legal_onto.owl")

# Define the updated SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?restriction ?property ?constraintType ?constraintValue
WHERE {
    <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#Joint_Circulars> rdfs:subClassOf ?restriction .

    ?restriction owl:onProperty ?property .
    
    OPTIONAL { ?restriction owl:someValuesFrom ?constraintValue . BIND("someValuesFrom" AS ?constraintType) }
    OPTIONAL { ?restriction owl:minQualifiedCardinality ?constraintValue . BIND("minQualifiedCardinality" AS ?constraintType) }
    OPTIONAL { ?restriction owl:allValuesFrom ?constraintValue . BIND("allValuesFrom" AS ?constraintType) }
    OPTIONAL { ?restriction owl:qualifiedCardinality ?constraintValue . BIND("qualifiedCardinality" AS ?constraintType) }
}
"""

# Run the query
results = g.query(query)

# Print the results
for row in results:
    print(f"Restriction: {row.restriction}, Property: {row.property}, Constraint Type: {row.constraintType}, Value: {row.constraintValue}")
