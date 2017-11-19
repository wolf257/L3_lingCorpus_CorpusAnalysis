import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# print(PROJECT_ROOT) #nous donne la base du dossier

CORPUS_ROOT = os.path.join(PROJECT_ROOT, 'corpus/')
# print(CORPUS_ROOT)

CORPUS_TEST_ROOT = os.path.join(PROJECT_ROOT, 'corpus_test/')
# print(CORPUS_TEST_ROOT)

MORPHALO_ROOT = os.path.join(PROJECT_ROOT, 'morphalo/')
# print(MORPHALO_ROOT)

RESULT_RAPPORT_ROOT = os.path.join(PROJECT_ROOT, 'resultats_et_rapport/')
# print(RESULT_RAPPORT_ROOT)
