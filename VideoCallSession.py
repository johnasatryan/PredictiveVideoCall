# This Python file uses the following encoding: utf-8

from typing import List
from CameraWindow import CameraWindow

class CallRecords:
    # Placeholder for CallRecords definition
    pass

class VideoCallSession:
    def __init__(self, ui):
        self.__participants: List[str] = []
        self.__sessionTopic:str = ""
        self.__callHistory: List[CallRecords] = []
        self.__startTime = None
        self.__endTime = None
        self.window = CameraWindow(ui)

    def addParticipant(self, user: str):
        self.__participants.append(user)

    def removeParticipant(self, userId:str):
        pass

    def initialCall(self):
        pass


