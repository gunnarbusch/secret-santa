import unittest
from os import listdir, path
from shutil import rmtree

from secretSanta import SecretSantaDrawer


testCfg = {
    "output_folder": "test_ouput",
    "participants": ["A", "B", "C", "D", "E", "F"],
    "not_together": [["A", "F"]],
    "output_message": "{name}:{partner}"
}


class SecretSantaTest(unittest.TestCase):
    def setUp(self):
        self.secretSanta = SecretSantaDrawer(
            testCfg["output_folder"], 
            testCfg["participants"],  
            testCfg["not_together"], 
            testCfg["output_message"]
        )

        self.secretSanta.startDraw()

    def tearDown(self):
        rmtree(testCfg["output_folder"])

    def testFolderStructure(self):
        self.assertEqual(path.exists(testCfg["output_folder"]), True, 
            "Output folder should exist")

        filesInFolder = listdir(testCfg["output_folder"])
        self.assertEqual(len(filesInFolder), len(testCfg["participants"]), 
            "Should have correct amount of output files")

        fileNamesStriped = [fn[:-4] for fn in filesInFolder]
        self.assertEqual(sorted(fileNamesStriped) == testCfg["participants"], True, 
            "Should have a file for each participant")

    def testFileContent(self):
        for name, fileConent in self._readEachFile():
            contentSplit = fileConent.split(":")
            contentName = contentSplit[0]
            contentPartner = contentSplit[1]

            self.assertRegex(fileConent, "^[A-Z]:[A-Z]$", 
                "Should have correct output format")

            self.assertEqual(name, contentName, 
                "Should have same file name on name in file content")

            self.assertNotEqual(contentName, contentPartner, 
                "Should not have same name and partner")

            if contentName == "A":
                self.assertNotEqual(contentPartner, "F", 
                    "Should have not partner (F) that are marked as not together")

            if contentName == "F":
                self.assertNotEqual(contentPartner, "A", 
                    "Should have not partner (A) that are marked as not together")

    def _readEachFile(self):
         for filename in listdir(testCfg["output_folder"]):
            name = filename[:-4]
            with open("{0}/{1}".format(testCfg["output_folder"], filename), "r") as testFile:
                yield name, testFile.read()


if __name__ == '__main__':
    unittest.main()
