
import json
import csv
from datetime import datetime


# Mixin 1 : Serializable
class Serializable:

    def to_json(self):
        donnees = {
            "id": self.id,
            "description": self.description
        }
        return json.dumps(donnees, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):
        donnees = json.loads(json_str)
        return cls(**donnees)


# Mixin 2 : Historisable
class Historisable:

    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        etat = {
            "id": self.id,
            "description": self.description
        }
        self.historique.append(etat.copy())


# Mixin 3 : Journalisable
class Journalisable:

    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")


# Mixin 4 : Horodatable
class Horodatable:

    def horodatage(self):
        return datetime.now().isoformat()


# Mixin 5 : ExportCSV
class ExportCSV:

    def exporter_csv(self, fichier):
        with open(fichier, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["id", "description"]
            )
            writer.writeheader()
            writer.writerow({
                "id": self.id,
                "description": self.description
            })


# Classe principale
class Contrat(
    Serializable,
    Historisable,
    Journalisable,
    Horodatable,
    ExportCSV
):

    def __init__(self, id, description):
        Historisable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")

        self.enregistrer_etat()

        self.description = nouvelle_desc

        print("Contrat modifié avec succès.")
