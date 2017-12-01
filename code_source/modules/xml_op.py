#from lxml import etree

import xml.etree.ElementTree as ET
from collections import defaultdict


## Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_TEST_ROOT, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

########################################################
# LIST FUNCTIONS IN MODULES
#	+ tagger_et_recuperer_as_dict + test
#	+
#	+
#	+
#	+
########################################################

folder_treetagger = TREETAGGER_ROOT

#ouvre le doc xml et le renvoie en objet
document_xml = ET.parse('/Users/gueyeousseynou/Dropbox/dropbox_cs/git_projects_on_line/projet_s5_ling_corpus/morphalo/morphalou-2.0.xml')

root = document_xml.getroot() # on est a lexion
root.tag # Nous rend lexicon
root.attrib # attrib {}

#SHOW only the ten first (sinon trop long)
#
i = 0
for child in root :
    if i > 10 :
        break
    else :
        print(child.tag, child.attrib)
        i += 1
# >>> lexicalEntry {'id': 'a_1'}
# >>> lexicalEntry {'id': 'a_b_c_1'}

i = 0
for child in root :
    if i > 10 :
        break
    else :
        print(child.tag, child.attrib)
        i += 1

#list des lexicalEntry
i = 0
for elt in root.iter(tag='lexicalEntry') :
    if i > 300 :
        break
    else :
        print(elt.tag, elt.attrib)
        i += 1

#list des tags
i = 0
for elt in root.iter() :
    if i > 300 :
        break
    else :
        print(elt.tag, elt.attrib)
        i += 1



root[0] #lexiconInfo : pas d'interet
root[1] #lexicalEntry : des boites de la forme
