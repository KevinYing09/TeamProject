#Isaac Cheung
class PackingItem:

  def __init__(self, itemId, name, category, assignedToUserId, isPacked):
    self.itemId = itemId
    self.name = name
    self.category = category
    self.assignedToUserId = assignedToUserId
    self.isPacked = isPacked

  def togglePackedStatus(self):
    pass
