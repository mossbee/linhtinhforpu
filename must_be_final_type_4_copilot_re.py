from rdflib import Graph, Namespace, RDF, RDFS, OWL, XSD, Literal

# Initialize the graph and load the OWL file
g = Graph()
g.parse("legal_onto.owl")  # Replace with the actual path to the .owl file

# Define the namespace for the ontology
ns = Namespace("http://www.semanticweb.org/ontologies/2024/8/legal_ontology#")

# Define the SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX : <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?agencies ?restrictionType ?restrictionProperty ?cardinalityValue
WHERE {
    :JointCircular rdfs:subClassOf ?restriction .
    ?restriction owl:onProperty :PromulgatedBy .

    # Check for unionOf and restrictions
    {
        ?restriction owl:onClass ?classRestriction .
        ?classRestriction owl:unionOf ?agencyCollection .
        ?agencyCollection rdf:rest*/rdf:first ?agencies .
        OPTIONAL {
            ?restriction owl:minQualifiedCardinality ?cardinalityValue .
            BIND("minQualifiedCardinality" AS ?restrictionType)
        }
        OPTIONAL {
            ?restriction owl:someValuesFrom ?someClass .
            BIND("someValuesFrom" AS ?restrictionType)
        }
        BIND("unionOf" AS ?restrictionProperty)
    }
}
"""

# Execute the query
qres = g.query(query)

# Process the result
results = []
current_entry = {}
agencies = []
for row in qres:
    agency = str(row.agencies.split('#')[-1])
    if agency not in agencies:
        agencies.append(agency)
    if row.restrictionType is not None:
        current_entry = {
            "Agencies": agencies,
            "Restriction Property": row.restrictionProperty,
            "Restriction Type": row.restrictionType,
            "Cardinality Value": row.cardinalityValue if row.cardinalityValue else None,
        }
        results.append(current_entry)
        agencies = []

# Output the result
results
