import os
import shutil
import unittest
from devops import garantir_diretorio, contar_arquivos_txt, DEVOPS_DIR


class TestDevOps(unittest.TestCase):

    def setUp(self):
        if os.path.exists(DEVOPS_DIR):
            shutil.rmtree(DEVOPS_DIR)
        os.makedirs(DEVOPS_DIR)

    def tearDown(self):
        if os.path.exists(DEVOPS_DIR):
            shutil.rmtree(DEVOPS_DIR)

    def test_diretorio_criado(self):
        garantir_diretorio()
        self.assertTrue(os.path.exists(DEVOPS_DIR))

    def test_contagem_txt(self):
        with open(os.path.join(DEVOPS_DIR, "teste.txt"), "w") as f:
            f.write("teste")

        total = contar_arquivos_txt()
        self.assertEqual(total, 1)


if __name__ == "__main__":
    unittest.main()
