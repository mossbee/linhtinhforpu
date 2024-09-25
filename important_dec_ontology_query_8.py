from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, OWL, XSD

# Load the RDF graph
g = Graph()
g.parse("legal_onto.owl", format="xml")

# Define namespaces
ns = Namespace("http://www.semanticweb.org/ontologies/2024/8/legal_ontology#")

# SPARQL query
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX ns: <http://www.semanticweb.org/ontologies/2024/8/legal_ontology#>

SELECT ?documentType ?agency ?cardinality
WHERE {
  ?documentType rdf:type owl:Class ;
                rdfs:subClassOf ?restriction .
  ?restriction rdf:type owl:Restriction ;
               owl:onProperty ns:canBePromulgatedBy ;
               (owl:onClass|owl:someValuesFrom|owl:allValuesFrom|owl:hasValue) ?agency .
  OPTIONAL {
    ?restriction (owl:qualifiedCardinality|owl:minQualifiedCardinality|owl:maxQualifiedCardinality) ?cardinality .
  }
  FILTER (?documentType = ns:YourDocumentType)
}
"""

# Replace 'YourDocumentType' with the actual document type URI
document_type_uri = ns.Joint_Circulars  # Example document type
query = query.replace("ns:YourDocumentType", f"<{document_type_uri}>")

# Execute the query
results = g.query(query)

# Print the results
for row in results:
    print(f"Document Type: {row.documentType}, Agency: {row.agency}, Cardinality: {row.cardinality}")