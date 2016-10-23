class Analytics:

    def __init__(self):
        self.data={}

    def addTags(self, tags):
        for i in tags:
            if i in self.data:
                self.data[i] =  self.data[i]+1
            else:
                self[i] = 1

    def getTagCounts(self):
        return self.data