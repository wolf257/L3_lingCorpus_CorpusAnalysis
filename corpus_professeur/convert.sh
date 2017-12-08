dossier=`pwd`

####################################
#	Conversion des fichiers
####################################
counter=1

for file in $dossier/*.pdf
do
    pdftotext -enc UTF-8 -eol unix $file;
    #echo "Conversion $file réussie" ;
    counter=$((counter+1));
done
echo "*** $counter fichiers ont été convertis du format pdf au format text."

#####################################
# Creation de dossier
####################################
mkdir pdf;
echo "*** Le dossier pdf a été créé."

####################################
# Déplacement des fichiers
####################################
find . -maxdepth 1 -name "*.pdf" -exec mv {} pdf/ \;
echo "*** Les fichiers pdf on été déplacé dans le dossier pdf."

echo "*** Les fichiers text sont à la racine du dossier."

#find . -maxdepth 1 -name "*.txt" -exec mv {} text/ \;
#echo -e "\n*** Les fichiers text on été déplacé dans le dossier text."
