import ROOT
import collections
import time

#======================================================================

class EventCounter(object):
    """Event counting faclility for the analysis class."""
    def __init__(self, name):
        super(EventCounter, self).__init__()
        self.Name = name
        self.RawCounter      = collections.Counter()
        self.WeightedCounter = collections.Counter()
    
    def printResults(self):
        self.log("+----------------------------------------------------------------+")
        for item, value in self.RawCounter.most_common():
            self.log("|%20s : %20i : %17.2f |" %(item, value, self.WeightedCounter[item]))
        self.log("+----------------------------------------------------------------+")
    
    def log(self, message):
        print time.ctime() + " EventStatistics " + self.Name + ": " + message
    
    # Utility function      
    def update(self, cut, weight):
        self.RawCounter[cut] += 1.0
        self.WeightedCounter[cut] += weight
        


class QuietEventCounter(EventCounter):
    """Event counting faclility for the analysis class."""
    def __init__(self):
        super(QuietEventCounter, self).__init__("Blank")
    
    def printResults(self):
        return
    
    def log(self, message):
        return
    
    def update(self, cut, weight):
        return