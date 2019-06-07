class Outing:
    def __init__(self, eventday, eventtype, costofevent, numberofpeople, costperperson):
        self.eventday = eventday
        self.eventtype = eventtype
        self.costofevent = costofevent
        self.numberofpeople = numberofpeople
        self.costperperson = costperperson

    def __repr__(self):
        return f"{self.eventday}                  {self.eventtype}                     {self.costofevent}     {self.numberofpeople}     {self.costperperson}"

