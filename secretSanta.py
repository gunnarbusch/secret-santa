
from os import path, makedirs
from random import choice
from datetime import datetime


class SecretSantaDrawer:
    def __init__(self, outputFolder, participants, notTogether, outputMessage):
        self.outputFolder = outputFolder
        self.participants = participants
        self.notTogether = notTogether
        self.outputMessage = outputMessage
        self._createFolderIfNotExists(outputFolder)

    def startDraw(self):
        try:
            availablePartners = self.participants.copy()
            for name in self.participants:
                partner = self._draw(name, availablePartners)
                self._writeToFile(name, partner)
                availablePartners.remove(partner)
        except ValueError as exp:
            print(exp)
            self.startDraw()

    def _draw(self, name, availablePartners):
        partner = choice(availablePartners)
        
        if partner == name:
            raise ValueError("Last name is own name! Restart...")

        for pair in self.notTogether:
            if len(set(pair) & set([name, partner])) > 1:
                raise ValueError("Last partner is one that should not be together! Restart...")

        return partner

    def _writeToFile(self, name, partner):
        with open("{0}/{1}.txt".format(self.outputFolder, name), "w") as f:
            msg = self.outputMessage.format(name=name, partner=partner)
            f.write(msg)

    def _createFolderIfNotExists(self, folderName):
        if not path.exists(folderName):
            makedirs(folderName)


if __name__ == "__main__":
    from config import cfg

    drawer = SecretSantaDrawer(
        cfg["output_folder"],
        cfg["participants"], 
        cfg["not_together"], 
        cfg["output_message"])

    drawer.startDraw()
