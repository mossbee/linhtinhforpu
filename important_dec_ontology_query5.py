from rdflib import Graph

# Load the OWL file
g = Graph()
g.parse("legal_onto.owl", format="xml")

# Define the SPARQL query to extract the onClass restriction for Constitution
query = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?onClass
WHERE {
    :Constitution rdfs:subClassOf ?restriction .
    ?restriction owl:onClass ?onClass .
}
"""

# Execute the query
results = g.query(query)

# Print the results
for row in results:
    print(f"onClass restriction for Constitution: {row.onClass}")
