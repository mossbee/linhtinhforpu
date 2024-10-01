from rdflib import Graph

# Load the ontology
g = Graph()
g.parse("legal_onto.owl")

# Define the SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?superClass WHERE {
  :Ministry_of_National_Defense rdfs:subClassOf ?superClass .
}
"""

# Execute the query
results = g.query(query)

# Process the results
for row in results:
    super_class = str(row.superClass)
    if super_class == "http://www.w3.org/2002/07/owl#Thing":
        print("Ministry_of_National_Defense")
    else:
        print(super_class)