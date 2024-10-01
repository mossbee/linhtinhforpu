from rdflib import Graph

# Load the OWL file
g = Graph()
g.parse("legal_onto.owl", format="xml")

# Define the SPARQL query to extract the agencies or unions of agencies that can promulgate Joint_Circulars
query = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?restriction ?agency
WHERE {
    :Joint_Circulars rdfs:subClassOf ?intersection .
    ?intersection owl:intersectionOf/rdf:rest*/rdf:first ?restriction .

    {
        ?restriction owl:onClass/owl:unionOf/rdf:rest*/rdf:first ?agency .
        ?restriction owl:onProperty :canBePromulgatedBy .
        ?restriction owl:minQualifiedCardinality ?minCardinality .
    }
    UNION
    {
        ?restriction owl:someValuesFrom/owl:unionOf/rdf:rest*/rdf:first ?agency .
        ?restriction owl:onProperty :canBePromulgatedBy .
    }
}
ORDER BY ?restriction
"""

# Execute the query
results = g.query(query)

# Group the results by restriction
from collections import defaultdict

grouped_agencies = defaultdict(list)
for row in results:
    grouped_agencies[str(row.restriction)].append(str(row.agency))

# Print the results
for restriction, agencies in grouped_agencies.items():
    print(f"Restriction: {restriction}")
    print("Agencies or unions of agencies that can promulgate Joint_Circulars:", agencies)
    print()