from owlready2 import *
import types

legal_onto = get_ontology("http://www.semanticweb.org/ontologies/2024/8/legal_ontology")

doc_type = [
    "Circulars",
    "Constitution",
    "Decisions",
    "Decrees",
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
    "Judicial Council of the Peoples Supreme Court",
    "President",
    "Peoples Supreme Court",
    "Supreme Peoples Court",
]

local_agencies = [
    "Peoples Council all levels",
    "Peoples Committees all levels"
]

people_councils = [
    "Peoples Council of Province",
    "Peoples Council of District",
    "Peoples Council of Commune"
]

people_committees = [
    "Peoples Committee of Province",
    "Peoples Committee of District",
    "Peoples Committee of Commune"
]

ministerial_level_agencies = [
    "Ministry of National Defense",
    "Ministry of Public Security",
    "Ministry of Foreign Affairs",
    "Ministry of Justice",
    "Ministry of Justice",
    "Ministry of Finance",
    "Ministry of Industry and Trade",
    "Ministry of Labor War Invalids and Social Affairs",
    "Ministry of Transport",
    "Ministry of Construction",
    "Ministry of Information and Communications",
    "Ministry of Education and Training",
    "Ministry of Agriculture and Rural Development",
    "Ministry of Planning and Investment",
    "Ministry of Home Affairs",
    "Ministry of Health",
    "Ministry of Science and Technology",
    "Ministry of Culture Sports and Toursm",
    "Ministry of Natural Resources and Environment",
    "Government Inspectorate",
    "The State Bank of Vietnam",
    "Committee for Ethnic Affairs",
    "Office of the Government"
]

with legal_onto:
    class Legal_Documents(Thing):
        pass
    class Legal_Normative_Document(Legal_Documents):
        pass
    class Agencies(Thing):
        pass
    class Central_Level_Agencies(Agencies):
        pass
    class Local_Level_Agencies(Agencies):
        pass

    for central_agency in central_agencies:
        central_agency = central_agency.replace(" ", "_")
        type(central_agency, (Central_Level_Agencies, ), {})
    for local_agency in local_agencies:
        local_agency = local_agency.replace(" ", "_")
        type(local_agency, (Local_Level_Agencies, ), {})
    Peoples_Council_all_levels = legal_onto.Peoples_Council_all_levels
    Peoples_Committees_all_levels = legal_onto.Peoples_Committees_all_levels
    for people_council in people_councils:
        people_council = people_council.replace(" ", "_")
        type(people_council, (Peoples_Council_all_levels, ), {})
    for people_committee in people_committees:
        people_committee = people_committee.replace(" ", "_")
        type(people_committee, (Peoples_Committees_all_levels, ), {})
    
    class Ministry_and_Ministerial_Level_Agencies(Central_Level_Agencies):
        pass
    for ministerial_level_agency in ministerial_level_agencies:
        ministerial_level_agency = ministerial_level_agency.replace(" ", "_")
        type(ministerial_level_agency, (Ministry_and_Ministerial_Level_Agencies, ), {})

    class canBePromulgatedBy(ObjectProperty):
        domain = [Legal_Documents]
        range = [Agencies]
        
National_Assembly = legal_onto.National_Assembly
Standing_Committee_of_the_National_Assembly = legal_onto.Standing_Committee_of_the_National_Assembly
Presidium_of_the_Central_Committee_of_the_Vietnam_Fatherland_Front = legal_onto.Presidium_of_the_Central_Committee_of_the_Vietnam_Fatherland_Front
Government = legal_onto.Government
Prime_Minister = legal_onto.Prime_Minister
State_Auditor = legal_onto.State_Auditor
Judicial_Council_of_the_Peoples_Supreme_Court = legal_onto.Judicial_Council_of_the_Peoples_Supreme_Court
Peoples_Council_all_levels = legal_onto.Peoples_Council_all_levels
Peoples_Committees_all_levels = legal_onto.Peoples_Committees_all_levels
President = legal_onto.President
Peoples_Supreme_Court = legal_onto.Peoples_Supreme_Court
Supreme_Peoples_Court = legal_onto.Supreme_Peoples_Court

# Constitution can only be promulgate by one National Assembly
class Constitution(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(1, National_Assembly)
    ]

# Laws one National Assembly
class Laws(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(1, National_Assembly)
    ]

# Ordinances one Standing Committee of the National Assembly
class Ordinances(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(1, Standing_Committee_of_the_National_Assembly)
    ]

# Resolutions one among National Assembly, Standing Committee of the National Assembly, Judicial Council of the Peoples Supreme Court, Peoples Council all levels
class Resolutions(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(1, National_Assembly | Standing_Committee_of_the_National_Assembly | Judicial_Council_of_the_Peoples_Supreme_Court | Peoples_Council_all_levels)
    ]

# Joint_Resolutions can only be promulgate by union (joint 3) of Standing Committee of the National Assembly, Presidium of the Central Committee of the Vietnam Fatherland Front and Government or union (joint 2) of Standing Committee of the National Assembly and Presidium of the Central Committee of the Vietnam Fatherland Front or union (joint 2) of Presidium of the Central Committee of the Vietnam Fatherland Front and Government
class Joint_Resolutions(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(3, Standing_Committee_of_the_National_Assembly | Presidium_of_the_Central_Committee_of_the_Vietnam_Fatherland_Front | Government) &
        canBePromulgatedBy.exactly(2, Standing_Committee_of_the_National_Assembly | Presidium_of_the_Central_Committee_of_the_Vietnam_Fatherland_Front) &
        canBePromulgatedBy.exactly(2, Presidium_of_the_Central_Committee_of_the_Vietnam_Fatherland_Front | Government)
    ]

# Orders can only be promulgate by one President
class Orders(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(1, President)
    ]

# Decrees can only be promulgate by one Government
class Decrees(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(1, Government)
    ]

# Decisions can only be promulgate by one among Prime Minister, State Auditor, Peoples Committee all levels, President
class Decisions(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(1, Prime_Minister | State_Auditor | Peoples_Committees_all_levels | President)
    ]

# Circulars can only be promulgate by one among Peoples Supreme Court, Ministry and Ministerial Level Agencies, Supreme Peoples Court
class Circulars(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.exactly(1, Peoples_Supreme_Court | Ministry_and_Ministerial_Level_Agencies | Supreme_Peoples_Court)
    ]

# Joint Circulars can only be promulgate by union (min 2) of State Auditor, Peoples Supreme Court, Supreme Peoples Court, Ministry and Ministerial Level Agencies and at least one of them are among State Auditor, Peoples Supreme Court, Supreme Peoples Court
class Joint_Circulars(Legal_Normative_Document):
    is_a = [
        canBePromulgatedBy.min(2, State_Auditor | Peoples_Supreme_Court | Supreme_Peoples_Court | Ministry_and_Ministerial_Level_Agencies) &
        canBePromulgatedBy.some(State_Auditor | Peoples_Supreme_Court | Supreme_Peoples_Court)
    ]

legal_onto.save(file="legal_onto.owl", format="rdfxml")