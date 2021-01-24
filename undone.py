_author__ = "Alix Boc"
__date__   = "hiver 2021"

""" Manipulation d'un compte bancaire utilisant un objet"""

from CompteBancaire_o2 import CompteBancaire

monCompte1 = CompteBancaire ( "12345", "Smith", "John", "111222333", "Montréal", 1000, 500 )
monCompte2 = CompteBancaire ( "12346", "Smith", "John", "111222333", "Montréal", 1000, 500 )

print(monCompte1["solde"])
