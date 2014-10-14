
import logging
import Mes_Modules.Fonctions
import Mes_Modules.arguments
import argparse
import sys
from Mes_Modules import Fonctions
from Mes_Modules.arguments import arguments_generals, arguments_optionnels


#logging.basicConfig(filename ="Journal_log.log", level = logging.DEBUG)
logging.basicConfig(level = logging.DEBUG)
logging.info("Mise en marche du programme")

arguments_generals
arguments_optionnels

# On affiche les arguments obligatoire
Mes_Modules.arguments.arguments_generals()
Mes_Modules.arguments.arguments_optionnels()
args = Mes_Modules.arguments.parser.parse_args()
logging.info(repr(args))

Fonctions.verification_du_temps(args.dureePlaylist)
args.genrePlaylist[1] = Mes_Modules.Fonctions.verifier_mes_quantite(args.genrePlaylist[1])
logging.info(repr(args))
#fonctions.gestion_Pourcentage()

#print(args)

#fonctions.aVoir()


#modules.arguments.args.genrePlaylist[1] = fonctions.verifier_mes_quantite(modules.arguments.args.genrePlaylist[1])

logging.info('Tout a été opérationel')
logging.info(' *****************FIN************************')
logging.shutdown()
exit(0)