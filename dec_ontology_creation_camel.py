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
    "Ministry Of National Defense",
    "Ministry Of Public Security",
    "Ministry Of Foreign Affairs",
    "Ministry Of Justice",
    "Ministry Of Justice",
    "Ministry Of Finance",
    "Ministry Of Industry And Trade",
    "Ministry Of Labor War Invalids And Social Affairs",
    "Ministry Of Transport",
    "Ministry Of Construction",
    "Ministry Of Information And Communications",
    "Ministry Of Education And Training",
    "Ministry Of Agriculture And Rural Development",
    "Ministry Of Planning And Investment",
    "Ministry Of Home Affairs",
    "Ministry Of Health",
    "Ministry Of Science And Technology",
    "Ministry Of Culture Sports And Tourism",
    "Ministry Of Natural Resources And Environment",
    "Government Inspectorate",
    "The State Bank Of Vietnam",
    "Committee For Ethnic Affairs",
    "Office Of The Government"
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

    class PromulgatedBy(ObjectProperty):
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
        PromulgatedBy.exactly(1, NationalAssembly)
    ]

# Laws by one National Assembly
class Law(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.exactly(1, NationalAssembly)
    ]

# Ordinances by one Standing Committee Of the National Assembly
class Ordinance(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.exactly(1, StandingCommitteeOfTheNationalAssembly)
    ]

# Resolutions by one among National Assembly, Standing Committee Of the National Assembly, Judicial Council Of the Peoples Supreme Court, Peoples Council all levels
class Resolution(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.exactly(1, NationalAssembly | StandingCommitteeOfTheNationalAssembly | JudicialCouncilOfThePeopleSupremeCourt | PeoplesCouncilAllLevels)
    ]

# JointResolutions by union Of Standing Committee Of the National Assembly, Presidium Of the Central Committee Of the Vietnam Fatherland Front, and Government
class JointResolution(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.some(
            StandingCommitteeOfTheNationalAssembly & PresidiumOfTheCentralCommitteeOfTheVietnamFatherlandFront & Government |
            StandingCommitteeOfTheNationalAssembly & PresidiumOfTheCentralCommitteeOfTheVietnamFatherlandFront |
            PresidiumOfTheCentralCommitteeOfTheVietnamFatherlandFront & Government
        )
    ]

# Orders by one President
class Order(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.exactly(1, President)
    ]

# Decrees by one Government
class Decree(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.exactly(1, Government)
    ]

# Decisions by one among Prime Minister, State Auditor, Peoples Committee all levels, President
class Decision(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.exactly(1, PrimeMinister | StateAuditor | PeoplesCommitteesAllLevels | President)
    ]

# Circulars by one among Peoples Supreme Court, Ministry and Ministerial Level Agencies, Supreme Peoples Court
class Circular(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.exactly(1, PeopleSupremeCourt | MinistryMinisterialLevelAgencies | SupremePeopleProcuracy)
    ]

# JointCirculars by union Of State Auditor, Peoples Supreme Court, Supreme Peoples Court, Ministry and Ministerial Level Agencies
class JointCircular(LegalNormativeDocuments):
    is_a = [
        PromulgatedBy.min(2, StateAuditor | PeopleSupremeCourt | SupremePeopleProcuracy | MinistryMinisterialLevelAgencies) &
        PromulgatedBy.some(StateAuditor | PeopleSupremeCourt | SupremePeopleProcuracy)
    ]

legalOnto.save(file="legal_onto.owl", format="rdfxml")
