from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Dict

from topic import Topic


@dataclass
class UserTopics:
    user_id: str
    music: int
    sports: int
    politics: int
    corona: int
    food: int
    travel: int

    def increase_counters(self, counters: Dict[Topic, int]):
        for topic, count in counters.items():
            if topic == Topic.MUSIC:
                self.music += count
            elif topic == Topic.SPORTS:
                self.sports += count
            elif topic == Topic.POLITICS:
                self.politics += count
            elif topic == Topic.CORONA:
                self.corona += count
            elif topic == Topic.FOOD:
                self.food += count
            elif topic == Topic.TRAVEL:
                self.travel += count

    def to_dict(self) -> Dict[Topic, int]:
        return {
            Topic.MUSIC: self.music,
            Topic.SPORTS: self.sports,
            Topic.POLITICS: self.politics,
            Topic.CORONA: self.corona,
            Topic.FOOD: self.food,
            Topic.TRAVEL: self.travel,
        }

    def most_frequent(self) -> Topic:
        counters = self.to_dict()
        return max(counters, key=counters.get)


class BaseUserTopicsDB(metaclass=ABCMeta):
    @abstractmethod
    def initialize_topics(self, user_id: int):
        """
        Initialize (zeroed) topics for user.
        :param user_id: User ID to initialize its topics.
        """

    @abstractmethod
    def get_user_topics(self, user_id: int) -> UserTopics:
        """
        :param user_id: The ID of the user to get its topics count.
        :return: User's topics count.
        :raises UserNotExistingException: If no user with such ID exists.
        """

    @abstractmethod
    def update_user_topics(self, user_topics: UserTopics):
        pass
