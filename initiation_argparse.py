import argparse
import logging
import sys

logging.basicConfig(filename = "journal_log.log", level = logging.DEBUG)

parser = argparse.ArgumentParser()

parser.add_argument("dureePlaylist", type = int, help="duree de la playlist en minutes")
parser.add_argument("formatPlaylist", choices = ["m3u","xspf","pls"], help="format de sortie de la playlist")
parser.add_argument("nomFichierPlaylist", help="nom du fichier de sortie")


parser.add_argument("--T", "--titrePlaylist", help="titre choisis")
parser.add_argument("--a", "--artistePlaylist", help="nom de l'artiste")
parser.add_argument("--al", "--albumPlaylist", help="album présent dans la playlist")
parser.add_argument("--g", "--genrePlaylist", help="genre%pourcentage", nargs = 2)
parser.add_argument("--sg", "--sousGenrePlaylist", help="sousgenre%pourcentage", nargs = 2)

args = parser.parse_args()

Logging.info(args.dureePlaylist)
Logging.info(args.formatPlaylist)
Logging.info(args.nomFichierPlaylist)


def validerQuantite(quantite):
    try:
        logging.info("début du programme de verif")
        genre = abs(int(quantite))
        if 0 < genre > 100:
            raise Exception('Erreur')
        return genre
        logging.info("La saisie est correct")
    except ValueError:
        logging.error("La valeur saisie pour la quantité n'est pas une valeur numérique : '" + quantite + "'")
        exit(1)
    except Exception as err:
        if err.args[0] == 'Erreur':
            logging.error("La valeur saisie pour la quantité ne peut être négative : '%i'" % genre)
            exit(1)

args.genrePlaylist[1] = validerQuantite(args.genrePlaylist[1])


for argument in ['titrePlaylist','artistePlaylist','albumPlaylist','genrePlaylist']:
# Si l'argument est renseigné
    if getattr(args, argument) is not None:
        # On écrit la valeur de ses ss-arg dans le fichier de logs
        logging.info(' Argument --' + argument + ' :\t' + getattr(args, argument)[0] + ' ; ' + str(getattr(args, argument)[1]))
verifier_mes_quantite(getattr(args, argument))


logging.debug(' *****************************************')
logging.shutdown()
exit(0)

