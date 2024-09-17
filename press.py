from owlready2 import *
owlready2.JAVA_EXE = "C:\Program Files (x86)\Java\jre1.8.0_421\bin\java.exe"

from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

with onto:
    class Drug(Thing):
        def take(self): print("I took a drug")

    class ActivePrinciple(Thing):
        pass

    class has_for_active_principle(Drug >> ActivePrinciple):
        python_name = "active_principles"

    class Placebo(Drug):
        equivalent_to = [Drug & Not(has_for_active_principle.some(ActivePrinciple))]
        def take(self): print("I took a placebo")

    class SingleActivePrincipleDrug(Drug):
        equivalent_to = [Drug & has_for_active_principle.exactly(1, ActivePrinciple)]
        def take(self): print("I took a drug with a single active principle")

    class DrugAssociation(Drug):
        def take(self): print("I took a drug with %s active principles" % len(self.active_principles))
        equivalent_to = [Drug & has_for_active_principle.min(2, ActivePrinciple)]

acetaminophen   = ActivePrinciple("acetaminophen")
amoxicillin     = ActivePrinciple("amoxicillin")
clavulanic_acid = ActivePrinciple("clavulanic_acid")

AllDifferent([acetaminophen, amoxicillin, clavulanic_acid])

drug1 = Drug(active_principles = [acetaminophen])
drug2 = Drug(active_principles = [amoxicillin, clavulanic_acid])
drug3 = Drug(active_principles = [])

close_world(Drug)

with onto:
    sync_reasoner()