from rdflib import Graph

# Load the ontology
g = Graph()
g.parse("legal_onto.owl", format="xml")

# Define the SPARQL query to extract the agencies that can promulgate Joint_Resolutions
query = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?intersection ?agency
WHERE {
    :Joint_Resolutions rdfs:subClassOf ?restriction .
    ?restriction owl:someValuesFrom/owl:unionOf/rdf:rest*/rdf:first ?intersection .
    ?intersection owl:intersectionOf/rdf:rest*/rdf:first ?agency .
}
"""

# Execute the query
results = g.query(query)

# Collect the agencies in a dictionary where the key is the intersection and the value is a list of agencies
intersections = {}
for row in results:
    intersection = str(row.intersection)
    agency = str(row.agency)
    if intersection not in intersections:
        intersections[intersection] = []
    intersections[intersection].append(agency)

# Convert the dictionary values to a list of lists
agency_lists = list(intersections.values())

# Print the results
print("Agencies that can promulgate Joint_Resolutions:", agency_lists)