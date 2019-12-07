# %%
import pandas as pd

# %%
data = pd.read_csv("stage.csv")

# %%

print("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>")

print("<stages>")

for index, stage in data.iterrows():
    print("<stage>")
    print("<fonction >%s</fonction>" % stage["objet_social"])
    print("<etudiant>")
    print("<nom>%s</nom>" % stage["nom_etudiant"])
    print("<prenom>%s</prenom>" % stage["prenom_etudiant"])
    print("<section>%s</section>" % stage["section"])
    print("<classe>%s</classe>" % stage["classe"])
    print("</etudiant>")
    print("<entreprise>")
    print("<nom>%s</nom>" % stage["nom_societe"])
    print("<adresse>")
    print("<localite>%s</localite>" % stage["localite"])
    print("<nom>%s</nom>" % stage["adresse"].split(",")[0])
    print("<numero>%s</numero>" % stage["adresse"].split(",")[1])
    print("<codepostal>%s</codepostal>" % stage["cp"])
    print("</adresse>")
    print("<tel>%s</tel>" % stage["tel"])
    print("<responsable-stagiaire>")
    print("<civilite>%s</civilite>" % stage["civilite_resp_sta"])
    print("<nom>%s</nom>" % stage["responsable_stagiaire"])
    print("</responsable-stagiaire>")
    print("<responsable-service>")
    print("<civilite>%s</civilite>" % stage["civilite_resp_serv"])
    print("<nom>%s</nom>" % stage["responsable_service"])
    print("</responsable-service>")
    print("</entreprise>")

    print("</stage>")

print("</stages>")


# %%
