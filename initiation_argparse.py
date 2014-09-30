import argparse
import logging
import sys

logging.basicConfig(filename = "journal_log.log", level = logging.DEBUG)

parser = argparse.ArgumentParser()

parser.add_argument("dureePlaylist", type = int, help="duree de la playlist en minutes")
parser.add_argument("formatPlaylist", choices = ["m3u","xspf","pls"], help="format de sortie de la playlist")
parser.add_argument("nomFichierPlaylist", help="nom du fichier de sortie")


parser.add_argument("--titrePlaylist", help="titre choisis")
parser.add_argument("--artistePlaylist", help="nom de l'artiste")
parser.add_argument("--albumPlaylist", help="album présent dans la playlist")
parser.add_argument("--genrePlaylist", help="genre%pourcentage", nargs = 2)
parser.add_argument("--sousGenrePlaylist", help="sousgenre%pourcentage", nargs = 2)

args = parser.parse_args()

logging.debug(args)

def validerQuantite(quantite):
    try:
        logging.info("début du programme de verif")
        good = int(quantite)
        if good <= 0:
            raise Exception('UnderGround')
        return good
        logging.info("La saisie est correct")
    except ValueError:
        logging.error("La valeur saisie pour la quantité n'est pas une valeur numérique : '" + quantite + "'")
        exit(1)
    except Exception as err:
        if err.args[0] == 'UnderGround':
            logging.error("La valeur saisie pour la quantité ne peut être négative : '%i'" % genre)
            exit(1)

args.genrePlaylist[1] = validerQuantite(args.genrePlaylist[1])






