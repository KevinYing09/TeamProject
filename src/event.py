from datetime import datetime
from typing import Optional


class Event:

  def __init__(
      self,
      event_id: str,
      title: str,
      start_time: datetime,
      end_time: datetime,
      location: str,
      estimated_cost: float,
      category: str,
  ):
    self.event_id: str = event_id
    self.title: str = title
    self.start_time: datetime = start_time
    self.end_time: datetime = end_time
    self.location: str = location
    self.estimated_cost: float = estimated_cost
    self.category: str = category

  def update_event(
      self,
      title: Optional[str] = None,
      start_time: Optional[datetime] = None,
      end_time: Optional[datetime] = None,
      location: Optional[str] = None,
      estimated_cost: Optional[float] = None,
      category: Optional[str] = None,
  ) -> None:
    
    if title is not None:
      self.title = title
    if start_time is not None:
      self.start_time = start_time
    if end_time is not None:
      self.end_time = end_time
    if location is not None:
      self.location = location
    if estimated_cost is not None:
      self.estimated_cost = estimated_cost
    if category is not None:
      self.category = category

  def to_dict(self) -> dict:
    return {
        "eventId": self.event_id,
        "title": self.title,
        "startTime": self.start_time.isoformat(),
        "endTime": self.end_time.isoformat(),
        "location": self.location,
        "estimatedCost": self.estimated_cost,
        "category": self.category,
    }

  @classmethod
  def from_dict(cls, data: dict) -> "Event":
    return cls(
        event_id=data["eventId"],
        title=data["title"],
        start_time=datetime.fromisoformat(data["startTime"]),
        end_time=datetime.fromisoformat(data["endTime"]),
        location=data["location"],
        estimated_cost=float(data["estimatedCost"]),
        category=data["category"],
    )
