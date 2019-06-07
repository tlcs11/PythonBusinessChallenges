class Claim:
    def __init__(self, claimid, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid):
        self.claimid = claimid
        self.claimtype = claimtype
        self.description = description
        self.claimamount = claimamount
        self.dateofincident = dateofincident
        self.dateofclaim = dateofclaim
        self.isvalid = isvalid 


    def __repr__(self):
        return f"{self.claimid}          {self.claimtype}             {self.claimamount}     {self.dateofincident}     {self.dateofclaim}        {self.isvalid}     {self.description}"