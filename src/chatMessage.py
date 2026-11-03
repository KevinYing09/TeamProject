#Yicheng Deng
#Add import statements for other classes once complete
import datetime
class ChatMessage:
  def __init__(self, messageID, senderID, messagetext,time):
      self.messageID = messageID
      self.senderID = senderID
      self.messagetext = messagetext
      self.time = datetime.timestamp()

