class Client:
    def __init__(self, clientId: int, clientName: str, contactInfo: str, policyId: int):
        self.__clientId = clientId
        self.__clientName = clientName
        self.__contactInfo = contactInfo
        self.__policyId = policyId

    # Getters and Setters for clientId, clientName, contactInfo, and policyId
    def get_clientId(self):
        return self.__clientId

    def set_clientId(self, clientId):
        self.__clientId = clientId

    def get_clientName(self):
        return self.__clientName

    def set_clientName(self, clientName):
        self.__clientName = clientName

    def get_contactInfo(self):
        return self.__contactInfo

    def set_contactInfo(self, contactInfo):
        self.__contactInfo = contactInfo

    def get_policyId(self):
        return self.__policyId

    def set_policyId(self, policyId):
        self.__policyId = policyId

    def __str__(self):
        return f"Client[ID={self.__clientId}, Name={self.__clientName}, Contact={self.__contactInfo}, PolicyID={self.__policyId}]"
