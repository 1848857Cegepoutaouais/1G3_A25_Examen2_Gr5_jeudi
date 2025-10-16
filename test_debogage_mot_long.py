from debogage_mot_long import mot_plus_long, pourcentage_mots_max  # Remplacer par le nom de ton fichier

# ============================
# Tests pour mot_plus_long
# ============================
# TODO: Tests unitaires pour la fonction mot_plus_long (maximum 5 différents)
def test_mot_plus_long_normal():
    liste_mots = ["banane","orange","anticonstitutionnellement","pommes","celeri"]
    resultat = mot_plus_long(liste_mots)

    assert resultat == "anticonstitutionnellement"


def test_mot_plus_long_liste_vide():
    liste_mots = ["","","","",""]
    resultat = mot_plus_long(liste_mots)

    assert resultat is None


def test_mot_plus_long_str():
    liste_mots = "ALLO"
    resultat = mot_plus_long(liste_mots)

    assert resultat == "A"


def test_mot_plus_long_int():
    liste_mots = 99
    resultat = mot_plus_long(liste_mots)

    assert resultat is None


def test_mot_plus_long_spacial():
    liste_mots = ["néant","spacial","quasar", 3.14,"planétoïde"]
    resultat = mot_plus_long(liste_mots)

    assert resultat == "planétoïde"


# ============================
# Tests pour pourcentage_mots_max
# ============================
def test_pourcentage_mots_max_normal():
    mots = ["poney", "girafe", "hippopotame", "chaton"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 75.0

def test_pourcentage_mots_max_tous_superieur():
    """
    Lorsque tous les mots présents dépassent la taille,
    le pourcentage retourné est 100%.
    """
    # TODO: Complèter ce test unitaire.
    mots = ["éléphant", "hippopotame", "girafe"]
    resultat = pourcentage_mots_max(mots, 4)

    assert resultat == 100 # le résultat doit être 100%.

def test_pourcentage_mots_max_elements_invalides():
    mots = ["pamplemousse", 42, "cacahuète", None]
    resultat = pourcentage_mots_max(mots, 8)

    assert resultat == 100.0

def test_pourcentage_mots_max_liste_vide():
    mots = []
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat is None

def test_pourcentage_mots_max_tous_inferieur():
    """
    Lorsque tous les mots présents sont
    plus petits que la taille, le pourcentage
    retourné est 0.0%.
    """
    # TODO: Ajouter le cas de test correspondant à la description
    #       au plan de tests et complèter ce test unitaire.
    mots = ["chat", "chien", "rat"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 0.0

def test_pourcentage_mots_max_tous_str():
    mots = "chat"
    resultat = pourcentage_mots_max(mots, 3)

    assert resultat is None