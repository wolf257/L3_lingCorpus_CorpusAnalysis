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

echo "$counter fichiers ont été convertis du format pdf au format text."

#####################################
# Creation de dossier
####################################
mkdir text pdf;
echo -e "*** Les dossiers pdf et text ont été créés."

####################################
# Déplacement des fichiers
####################################
find . -maxdepth 1 -name "*.pdf" -exec mv {} pdf/ \;
echo -e "\n*** Les fichiers pdf on été déplacé dans le dossier pdf."

find . -maxdepth 1 -name "*.txt" -exec mv {} text/ \;
echo -e "\n*** Les fichiers text on été déplacé dans le dossier text."
