
from datetime import datetime
import copy


# Mixin 1 : Validation
class ValidationMixin:

    def valider(self):
        if not self.titre or not self.titre.strip():
            raise ValueError("Le titre est obligatoire.")


# Mixin 2 : Historique
class HistoriqueMixin:

    def __init__(self):
        self.historique = []

    def enregistrer_historique(self):
        ancienne_version = copy.deepcopy(self.description)
        self.historique.append(ancienne_version)

    def afficher_historique(self):
        print("Historique des descriptions :")
        for version in self.historique:
            print("-", version)


# Mixin 3 : Journalisation
class JournalisationMixin:

    def journaliser(self, action):
        print(f"[Journal] {datetime.now()} : {action}")


# Classe principale
class Tache(
    ValidationMixin,
    HistoriqueMixin,
    JournalisationMixin
):

    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()

        self.valider()
        HistoriqueMixin.__init__(self)

        self.journaliser(f"Création de la tâche '{self.titre}'")

    def mettre_a_jour(self, description):
        self.enregistrer_historique()

        self.description = description

        self.journaliser(
            f"Modification de la tâche '{self.titre}'"
        )


# Programme principal
tache = Tache(
    "Projet Python",
    "Apprendre les classes"
)

tache.mettre_a_jour("Apprendre les Mixins")

tache.mettre_a_jour("Créer un projet pratique")

print("\nDescription actuelle :")
print(tache.description)

print("\nDate de création :")
print(tache.date_creation)

print()
tache.afficher_historique()
