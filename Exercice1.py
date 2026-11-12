
from datetime import datetime
import json
from abc import ABC, abstractmethod


# Mixin 1 : Horodatable
class Horodatable:
    def horodatage(self):
        date = datetime.now()
        print(f"[LOG] Action à {date}")


# Mixin 2 : Validable
class Validable:
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")

        print("Validation OK")


# Mixin 3 : Serializable
class Serializable:
    def to_json(self):
        return json.dumps({
            "titre": self.titre,
            "contenu": self.contenu
        }, ensure_ascii=False)


# Mixin 4 : Historisable
class Historisable:
    def ajouter_action(self, action):
        if not hasattr(self, "historique"):
            self.historique = []

        self.historique.append({
            "action": action,
            "date": str(datetime.now())
        })

    def afficher_historique(self):
        for element in self.historique:
            print(element)


# Classe principale
class Document(
    Horodatable,
    Validable,
    Serializable,
    Historisable
):

    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
        self.historique = []

    def sauvegarder(self):
        self.horodatage()
        self.valider()
        self.ajouter_action("Sauvegarde")
        print(f"Document '{self.titre}' sauvegardé.")


# Utilisation
doc = Document("Rapport", "Contenu important")

doc.sauvegarder()

print("\nJSON :")
print(doc.to_json())

print("\nHistorique :")
doc.afficher_historique()
