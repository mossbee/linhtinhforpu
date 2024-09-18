import rdflib
from rdflib import URIRef, BNode

# Load the ontology
g = rdflib.Graph()
g.parse("legal_onto.owl", format="xml")  # Make sure to replace with your actual OWL file path

# Helper function to resolve blank nodes
def resolve_bnode(bnode, graph):
    """Recursively resolves a blank node into readable class or restriction."""
    if isinstance(bnode, BNode):
        resolved = []
        for s, p, o in graph.triples((bnode, None, None)):
            predicate = p.split('#')[-1]  # Get readable part of the URI
            if isinstance(o, BNode):
                # Recursively resolve blank nodes
                resolved.append(f"{predicate}: {resolve_bnode(o, graph)}")
            else:
                resolved.append(f"{predicate}: {o.split('#')[-1]}")
        return f"({', '.join(resolved)})"
    else:
        return bnode.split('#')[-1]  # Return human-readable part

# SPARQL query to get equivalent class and restrictions for Joint_Circulars
query = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?equivalentClass ?restriction
WHERE {
  # Find the class Joint_Circulars and its equivalent class
  ?jointCircular rdf:type owl:Class ;
                 owl:equivalentClass ?equivalentClass .

  # Ensure the subject is the #Joint_Circulars class
  FILTER (STR(?jointCircular) = "http://www.semanticweb.org/ontologies/2024/8/legal_ontology#Joint_Circulars")
  
  # Get restrictions if available
  OPTIONAL {
    ?equivalentClass owl:intersectionOf/rdf:rest*/rdf:first ?restriction .
  }
}
"""

# Execute the SPARQL query
result = g.query(query)

# Print results with human-readable format
for row in result:
    print(f"Equivalent Class: {resolve_bnode(row.equivalentClass, g)}")
    if row.restriction:
        print(f"Restriction: {resolve_bnode(row.restriction, g)}")