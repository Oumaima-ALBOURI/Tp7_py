
from contrat import Contrat

# Création
c = Contrat(1, "Initial")

# Modification
c.modifier("Révisé")

# Affichage JSON
print("\nJSON :")
print(c.to_json())

# Historique
print("\nHistorique :")
print(c.historique)

# Horodatage
print("\nDate :")
print(c.horodatage())

# Export CSV
c.exporter_csv("contrats.csv")
print("\nExport CSV terminé.")
