from tkinter import *
import mysql.connector

# se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chapy&Lapin",
  database="boutique"
)


# créer la fenêtre principale
root = Tk()
root.title("Tableau de bord de la boutique")

# créer la liste des produits
listbox = Listbox(root)
listbox.pack()

categorie_listbox = Listbox(root)
categorie_listbox.pack()

# récupérer les produits de la base de données
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM produit")
produits = mycursor.fetchall()

mycursor.execute("SELECT * FROM categorie")
categories = mycursor.fetchall()

# afficher les produits dans la liste
for produit in produits:
    listbox.insert(END, produit)
    
for categorie in categories:
    categorie_listbox.insert(END, categorie)

categorie_id = categories[categorie_listbox.curselection()[0]][0]

# créer un bouton pour ajouter un produit
def ajouter_produit():
    # ouvrir une nouvelle fenêtre pour ajouter un produit
    add_window = Toplevel()
    add_window.title("Ajouter un produit")

    # créer les champs pour le nouveau produit
    nom_label = Label(add_window, text="Nom")
    nom_label.grid(row=0, column=0)
    nom_entry = Entry(add_window)
    nom_entry.grid(row=0, column=1)

    description_label = Label(add_window, text="Description")
    description_label.grid(row=1, column=0)
    description_entry = Entry(add_window)
    description_entry.grid(row=1, column=1)

    prix_label = Label(add_window, text="Prix")
    prix_label.grid(row=2, column=0)
    prix_entry = Entry(add_window)
    prix_entry.grid(row=2, column=1)

    quantite_label = Label(add_window, text="Quantité")
    quantite_label.grid(row=3, column=0)
    quantite_entry = Entry(add_window)
    quantite_entry.grid(row=3, column=1)

    categorie_label = Label(add_window, text="Catégorie")
    categorie_label.grid(row=4, column=0)
    categorie_entry = Entry(add_window)
    categorie_entry.grid(row=4, column=1)

    # créer un bouton pour ajouter le produit
    def ajouter():
        nom = nom_entry.get()
        description = description_entry.get()
        prix = int(prix_entry.get())
        quantite = int(quantite_entry.get())
        categorie_id = categories[categorie_listbox.curselection()[0]][0]
        mycursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)", (nom, description, prix, quantite, categorie_id))
        mydb.commit()
        add_window.destroy()

    ajouter_button = Button(add_window, text="Ajouter", command=ajouter)
    ajouter_button.grid(row=5, column=0, columnspan=2)

# créer un bouton pour supprimer un produit
def supprimer_produit():
    index = listbox.curselection()[0]
    produit = produits[index]
    mycursor.execute("DELETE FROM produit WHERE id = %s", (produit[0],))
    mydb.commit()
    list
