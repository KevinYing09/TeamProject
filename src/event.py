class Event:

  def __init__(
      self,
      eventId,
      title,
      startTime,
      endTime,
      location,
      estimatedCost,
      category,
  ):
    self.eventId = eventId
    self.title = title
    self.startTime = startTime
    self.endTime = endTime
    self.location = location
    self.estimatedCost = estimatedCost
    self.category = category

  def updateEvent(self):
    pass
