def mot_plus_long(liste_mots):
    """
    Retourne le mot le plus long d'une liste.
    Ignore les éléments qui ne sont pas des chaînes de caractères.

    :param liste_mots: liste de mots
    :return: le mot le plus long ou None si la liste est invalide ou vide
    """
    max_mot = ""
    try:
        for mot in liste_mots:
            try:
                if len(mot) > len(max_mot):
                    max_mot = mot
            except TypeError:
                pass

    except TypeError:
        print(f"Erreur. Impossible de trouver le mot le plus long dans {liste_mots}")

    if max_mot != "":
        return max_mot
    else:
        return None

def pourcentage_mots_max(mots, taille):
    """
    Calcule le pourcentage de mots ayant une longueur supérieure à une valeur donnée.

    :param mots: liste de mots
    :param taille: longueur minimale à comparer
    :return: pourcentage (float) de mots dépassant la taille, ou None si impossible
    """
    # Si mots n'est pas de type list
    if not isinstance(mots, list):
        print(f"Impossible de calculer le pourcentage. '{mots}' n'est pas une liste.")
        return None

    # TODO: Corriger les bogues dans le code suivant les erreurs relevées par les tests unitaires de cette fonction.
    #       Indice : chaque mot valide mérite d’être compté, et seuls ceux qui sont suffisamment grands font grimper ton pourcentage !
    total_valide = 0.0
    count_sup = 0.0
    for mot in mots:
        if isinstance(mot, str): # Vérifier que le mot est un string
            longueur = len(mot)
            total_valide += 1.0 # Ajouter un +1 à total_valide pour pouvoir avoir le total des entrées qui était des strings
            if longueur > taille: # Changer le < en > puisque qu'on veut entrer lorsque le mot est plus long que la taille indiquée
                count_sup += 1.0 # Augmenter de 1 le compte du nombre de string qui sont plus long que la taille indiquée

    # Si mots est totalement vide
    if total_valide <= 0: # Vérifier que la liste mots a des éléments valides
        print("Impossible de calculer le pourcentage. Aucun élément valide.")
        return None
    else:
        pourcentage = float(count_sup/total_valide) * 100
        return round(pourcentage, 1)

if __name__ == "__main__":
    animaux = ["chat", "chien", "éléphant", "souris", "hippopotame", 42, None, "oiseau"]
    print("Mot le plus long :", mot_plus_long(animaux))
    pourcentage = pourcentage_mots_max(animaux, 5)

    if pourcentage is not None:
        print("Pourcentage de mots de longueur maximale :", pourcentage, "%")
