class Message:
    def __init__(self, subject, body, isSpam, foldNum):
        self.__subject = subject
        self.__body = body
        self.__isSpam = isSpam
        self.__foldNum = foldNum
    
    def getSubject(self):
        return self.__subject
    
    def getBody(self):
        return self.__body
    
    def getAllWords(self):
        return self.__subject + self.__body
    
    def isSpam(self):
        return self.__isSpam
    
    def getFold(self):
        return self.__foldNum
    
    def __str__(self):
        return 'Subject: ' + str(self.__subject) + '\n' +\
               'Is spam: ' + str(self.__isSpam) + '\n' +\
               str(self.__body) + '\n'