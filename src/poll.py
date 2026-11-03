#Kevin Ying

class Poll:
  def __init__(self, pollID, question, createdByUserID, isClosed):
    self.pollID = pollID
    self.question = question
    self.createdByUserID = createdByUserID
    self.isClosed = isClosed

  def clossPoll(self):
    pass

class PollOption:
  def __init__(self, optionID, optionText, voteCount):
    self.optionID = optionID
    self.optionText = optionText
    self.voteCount = voteCount

  def castVote(self, userID):
    pass
  
