class Policy:
    def __init__(self, policyId: int, policyName: str, policyDetails: str):
        self.policyId = policyId
        self.policyName = policyName
        self.policyDetails = policyDetails

    # Getters and Setters (if needed)
    def get_policyId(self):
        return self.policyId

    def set_policyId(self, policyId):
        self.policyId = policyId

    def get_policyName(self):
        return self.policyName

    def set_policyName(self, policyName):
        self.policyName = policyName

    def get_policyDetails(self):
        return self.policyDetails

    def set_policyDetails(self, policyDetails):
        self.policyDetails = policyDetails

    def __str__(self):
        return f"Policy ID: {self.policyId}, Name: {self.policyName}, Details: {self.policyDetails}"
