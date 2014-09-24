import argparse
parser = argparse.ArgumentParser()

parser.add_argument("dureePlaylist", type = int, help="duree de la playlist en minutes")
parser.add_argument("formatPlaylist", choices = ["m3u","xspf","pls"], help="format de sortie de la playlist")
parser.add_argument("nomFichierPlaylist", help="nom du fichier de sortie")


parser.add_argument("--titrePlaylist", help="titre choisis")
parser.add_argument("--artistePlaylist", help="nom de l'artiste")
parser.add_argument("--albumPlaylist", help="album présent dans la playlist")
parser.add_argument("--genrePlaylist", help="genre%pourcentage")
parser.add_argument("--sousGenrePlaylist", help="genre%pourcentage")

args = parser.parse_args()

print("duree : " + str(args.dureePlaylist))
print("format : " + args.formatPlaylist)
print("nom du fichier : " +args.nomFichierPlaylist)
print("titres choisis : " +args.titrePlaylist)
print("artistes choisis : " +args.artistePlaylist)
print("album choisis : " +args.albumPlaylist)
print("genre choisis : " +args.genrePlaylist)
print("sous genre choisis : " +args.sousGenrePlaylist)
