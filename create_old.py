import owlready2
from owlready2 import *
import types

# create ontology
legal_onto = get_ontology("http://www.semanticweb.org/ontologies/2024/8/legal_ontology")

with legal_onto:
    class Legal_Documents(Thing):
        pass

with legal_onto:
    class Agencies(Thing):
        pass

with legal_onto:
    class Central_Level_Agencies(Agencies):
        pass

with legal_onto:
    class Province_Level_Agencies(Agencies):
        pass
    class District_Level_Agencies(Agencies):
        pass
    class Commune_Level_Agencies(Agencies):
        pass

with legal_onto:
    class Legal_Normative_Document(Legal_Documents):
        pass

doc_type = [
    "Circulars",
    "Constitution",
    "Decisions",
    "Decrees",
    "Joint Circulars",
    "Joint Resolutions",
    "Laws",
    "Ordinances",
    "Resolutions",
]
central_agencies = [
    "National Assembly",
    "Standing Committee of the National Assembly",
    "Presidium of the Central Committee of the Vietnam Fatherland Front",
    "Government",
    "Prime Minister",
    "State Auditor",
    "Judicial Council of the People's Supreme Court",
    "President",
    "People's Supreme Court",
    "Supreme People's Court",
]

province_agencies = [
    "People's Council of Province",
    "People's Committee of Province"
]

district_agencies = [
    "People's Council of District",
	"People's Committee of District"
]

commune_agencies = [
    "People's Council of Communes",
	"People's Committee of Communes"
]

ministerial_level_agencies = [
    "Ministry of National Defense",
    "Ministry of Public Security",
    "Ministry of Foreign Affairs",
    "Ministry of Justice",
    "Ministry of Justice",
    "Ministry of Finance",
    "Ministry of Industry and Trade",
    "Ministry of Labor, War Invalids and Social Affairs",
    "Ministry of Transport",
    "Ministry of Construction",
    "Ministry of Information and Communications",
    "Ministry of Education and Training",
    "Ministry of Agriculture and Rural Development",
    "Ministry of Planning and Investment",
    "Ministry of Home Affairs",
    "Ministry of Health",
    "Ministry of Science and Technology",
    "Ministry of Culture, Sports and Toursm",
    "Ministry of Natural Resources and Environment",
    "Government Inspectorate",
    "The State Bank of Vietnam",
    "Committee for Ethnic Affairs",
    "Office of the Government"
]

with legal_onto:
	for doc in doc_type:
		doc = doc.replace(" ", "_")
		type(doc, (Legal_Normative_Document,), {})

with legal_onto:
    for central_agency in central_agencies:
        central_agency = central_agency.replace(" ", "_")
        type(central_agency, (Central_Level_Agencies, ), {})
    for local_agency in province_agencies:
        local_agency = local_agency.replace(" ", "_")
        type(local_agency, (Province_Level_Agencies, ), {})
    for local_agency in district_agencies:
        local_agency = local_agency.replace(" ", "_")
        type(local_agency, (District_Level_Agencies, ), {})
    for local_agency in commune_agencies:
        local_agency = local_agency.replace(" ", "_")
        type(local_agency, (Commune_Level_Agencies, ), {})

with legal_onto:
	class Ministry_and_Ministerial_Level_Agencies(Central_Level_Agencies):
		pass

with legal_onto:
	for ministerial_level_agency in ministerial_level_agencies:
		ministerial_level_agency = ministerial_level_agency.replace(" ", "_")
		type(ministerial_level_agency, (Ministry_and_Ministerial_Level_Agencies, ), {})

# save ontology
legal_onto.save(file="legal_onto.owl", format="rdfxml")