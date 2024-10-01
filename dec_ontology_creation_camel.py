from owlready2 import *
import types

legalOnto = get_ontology("http://www.semanticweb.org/ontologies/2024/8/legal_ontology")

centralAgencies = [
    "National Assembly",
    "Standing Committee Of The National Assembly",
    "Presidium Of The Central Committee Of The Vietnam Fatherland Front",
    "Government",
    "Prime Minister",
    "State Auditor",
    "Judicial Council Of The People Supreme Court",
    "President",
    "People Supreme Court",
    "Supreme People Procuracy",
]

localAgencies = [
    "People Council",
    "People Committee"
]

peopleCouncils = [
    "Provincial People Council",
    "District People Council",
    "Commune People Council"
]

peopleCommittees = [
    "Provincial People Committee",
    "District People Committee",
    "Commune People Committee"
]

ministerialLevelAgencies = [
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
    "Ministry of Culture Sports and Tourism",
    "Ministry of Natural Resources and Environment",
    "Government Inspectorate",
    "The State Bank of Vietnam",
    "Committee for Ethnic Affairs",
    "Office of the Government"
]

with legalOnto:
    class LegalDocuments(Thing):
        pass
    class LegalNormativeDocuments(LegalDocuments):
        pass
    class Agencies(Thing):
        pass
    class CentralLevelAgencies(Agencies):
        pass
    class LocalLevelAgencies(Agencies):
        pass

    for centralAgency in centralAgencies:
        centralAgency = centralAgency.replace(" ", "")
        type(centralAgency, (CentralLevelAgencies, ), {})
    for localAgency in localAgencies:
        localAgency = localAgency.replace(" ", "")
        type(localAgency, (LocalLevelAgencies, ), {})
    PeoplesCouncilAllLevels = legalOnto.PeopleCouncil
    PeoplesCommitteesAllLevels = legalOnto.PeopleCommittee
    for peopleCouncil in peopleCouncils:
        peopleCouncil = peopleCouncil.replace(" ", "")
        type(peopleCouncil, (PeoplesCouncilAllLevels, ), {})
    for peopleCommittee in peopleCommittees:
        peopleCommittee = peopleCommittee.replace(" ", "")
        type(peopleCommittee, (PeoplesCommitteesAllLevels, ), {})

    class MinistryMinisterialLevelAgencies(CentralLevelAgencies):
        pass
    for ministerialLevelAgency in ministerialLevelAgencies:
        ministerialLevelAgency = ministerialLevelAgency.replace(" ", "")
        type(ministerialLevelAgency, (MinistryMinisterialLevelAgencies, ), {})

    class CanBePromulgatedBy(ObjectProperty):
        domain = [LegalDocuments]
        range = [Agencies]
        
NationalAssembly = legalOnto.NationalAssembly
StandingCommitteeOfTheNationalAssembly = legalOnto.StandingCommitteeOfTheNationalAssembly
PresidiumOfTheCentralCommitteeOfTheVietnamFatherlandFront = legalOnto.PresidiumOfTheCentralCommitteeOfTheVietnamFatherlandFront
Government = legalOnto.Government
PrimeMinister = legalOnto.PrimeMinister
StateAuditor = legalOnto.StateAuditor
JudicialCouncilOfThePeopleSupremeCourt = legalOnto.JudicialCouncilOfThePeopleSupremeCourt
PeoplesCouncilAllLevels = legalOnto.PeopleCouncil
PeoplesCommitteesAllLevels = legalOnto.PeopleCommittee
President = legalOnto.President
PeopleSupremeCourt = legalOnto.PeopleSupremeCourt
SupremePeopleProcuracy = legalOnto.SupremePeopleProcuracy

# Constitutions can only be promulgated by one National Assembly
class Constitution(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.exactly(1, NationalAssembly)
    ]

# Laws by one National Assembly
class Law(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.exactly(1, NationalAssembly)
    ]

# Ordinances by one Standing Committee of the National Assembly
class Ordinance(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.exactly(1, StandingCommitteeOfTheNationalAssembly)
    ]

# Resolutions by one among National Assembly, Standing Committee of the National Assembly, Judicial Council of the Peoples Supreme Court, Peoples Council all levels
class Resolution(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.exactly(1, NationalAssembly | StandingCommitteeOfTheNationalAssembly | JudicialCouncilOfThePeopleSupremeCourt | PeoplesCouncilAllLevels)
    ]

# JointResolutions by union of Standing Committee of the National Assembly, Presidium of the Central Committee of the Vietnam Fatherland Front, and Government
class JointResolution(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.some(
            StandingCommitteeOfTheNationalAssembly & PresidiumOfTheCentralCommitteeOfTheVietnamFatherlandFront & Government |
            StandingCommitteeOfTheNationalAssembly & PresidiumOfTheCentralCommitteeOfTheVietnamFatherlandFront |
            PresidiumOfTheCentralCommitteeOfTheVietnamFatherlandFront & Government
        )
    ]

# Orders by one President
class Order(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.exactly(1, President)
    ]

# Decrees by one Government
class Decree(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.exactly(1, Government)
    ]

# Decisions by one among Prime Minister, State Auditor, Peoples Committee all levels, President
class Decision(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.exactly(1, PrimeMinister | StateAuditor | PeoplesCommitteesAllLevels | President)
    ]

# Circulars by one among Peoples Supreme Court, Ministry and Ministerial Level Agencies, Supreme Peoples Court
class Circular(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.exactly(1, PeopleSupremeCourt | MinistryMinisterialLevelAgencies | SupremePeopleProcuracy)
    ]

# JointCirculars by union of State Auditor, Peoples Supreme Court, Supreme Peoples Court, Ministry and Ministerial Level Agencies
class JointCircular(LegalNormativeDocuments):
    is_a = [
        CanBePromulgatedBy.min(2, StateAuditor | PeopleSupremeCourt | SupremePeopleProcuracy | MinistryMinisterialLevelAgencies) &
        CanBePromulgatedBy.some(StateAuditor | PeopleSupremeCourt | SupremePeopleProcuracy)
    ]

legalOnto.save(file="legal_onto.owl", format="rdfxml")
