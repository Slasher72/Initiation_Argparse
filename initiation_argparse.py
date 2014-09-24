import argparse
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

def validerQuantite(quantite):
    try:
        good = int(quantite)
        return good
    except ValueError:
        print("La valeur saisie n'est pas un entier : '" + quantite + "'")
        exit(1)

args.genrePlaylist[1] = validerQuantite(args.genrePlaylist[1])


if args.genrePlaylist[1] > 0 and args.genrePlaylist[1] <= 100:
    print(args)
else:
    print("le pourcentage doit être compris entre 0 et 100")




