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


def validerQuantite(arg, nomarg):
    logging.info("verifie argument 2")
    try:
        arg[1] = int(arg[1])
        if arg[1]<0:
            arg[1] = abs(arg[1])
            logging.warning('La quantité saisie doit etre positive')
            logging.info('Nombre négatif transformé en positif: ' + str(arg[1]))
        elif arg[1]>100:
            arg[1] = None
            logging.warning('La quantité saisie est supérieur à 100')
            logging.info('Nombre supérieur à 100 transformé en : ' + str(arg[1]))
        return True
    setattr(arg, nomarg, [arg[0], nomarg[1]])
    except ValueError:
        print ("Impossible de convertir \"" + arg[1] + "\" en nombre entier !")
        logging.error('Impossible de convertir ' + arg[1] + ' en nombre entier !')
        logging.debug(' *****************************************')
        exit(1)

if validerQuantite(args.genrePlaylist, args.genrePlaylist[1]):
    print ('ok')

print (type(args.genrePlaylist[1]))




