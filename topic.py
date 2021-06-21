from enum import Enum, auto
from typing import List, Dict


class Topic(str, Enum):
    MUSIC = 'music'
    SPORTS = 'sports'
    POLITICS = 'politics'
    CORONA = 'corona'
    FOOD = 'food'
    TRAVEL = 'travel'


# TODO: Make words lower
TOPIC_WORDS_MAPPING = {
    Topic.MUSIC: [
        'music', 'pop', 'hop', 'rap', 'Mizrahi', 'james', 'arthur', 'ariana', 'grande', 'shawn', 'mendes', 'justin',
        'bieber', 'billie', 'eilish', 'post', 'malone', 'noa', 'kirel', 'static', 'eden', 'hason', 'itay', 'levi',
        'demi', 'lovato', 'katy', 'perry', 'singers', 'songs', 'album', 'concert', 'bob', 'marley', 'dylan', 'drake',
        'khalid', 'imagine', 'dragons', 'bruno', 'mars', 'halsey', 'lipa', 'adele', 'lady', 'gaga', 'rihanna',
        'charlie', 'puth', 'beyonce', 'chainsmokers', 'weeknd', 'shakira', 'eminem', 'sia', 'direction', 'harry',
        'styles', 'miley', 'cyrus', 'sabrina', 'carpenter', 'elvis', 'eliad', 'nachum', 'Dudu', 'Faruk', 'nathan',
        'goshen', 'idan', 'amedi', 'osher', 'cohen', 'ishay', 'ribo', 'liran', 'danino', 'roni', 'dalumi', 'shiri',
        'maimon', 'omer', 'adam', 'matti', 'caspi', 'fortis', 'eyal', 'golan', 'gidi', 'gov', 'ivry', 'lider', 'harel',
        'skaat', 'shlomi', 'shabat',
    ],
    Topic.SPORTS: [
        'sports', 'deni', 'avedija', 'penalty', 'ball', 'base', 'baseball', 'basketball', 'champion', 'macabi',
        'hapoel', 'exercise', 'running', 'game', 'hockey', 'handball', 'bike', 'boxer', 'score', 'competition',
        'player', 'championship', 'coach', 'football', 'messi', 'david', 'beckham', 'cristiano', 'ronaldo',
        'maradona', 'neymar', 'ronaldinho', 'lebron', 'james', 'jordan', 'kobe', 'bryant', 'goal', 'soccer'
    ],
    Topic.POLITICS: [
        'netanyahu', 'benny', 'gantz', 'yair', 'lapid', 'naftali', 'bennett', 'left', 'right', 'likud', 'benjamin',
        'bibi', 'politics', 'government', 'election', 'yamina', 'politician', 'abbas', 'Gideon', 'saar', 'yesh',
        'atid', 'avigdor', 'lieberman', 'mansour', 'merav', 'michaeli', 'smotrich', 'mandate', 'minister',
        'Knesset', 'coalition', 'opposition', 'votes', 'vote', 'rotation', 'tibi', 'ahmad', 'party', 'Palestinian',
        'Balfour', 'dictator', 'demonstration', 'protest', 'immoral', 'trial', 'case', 'center', 'camp', 'wing'
    ],
    Topic.CORONA: [
        'corona', 'covid', 'virus', 'fever', 'breath', 'distance', 'mask', 'meters', 'spread', 'quarantine',
        'epidemic', 'vaccine', 'health', 'patient', 'sick', 'dead', 'death', 'green', 'tav', 'capsule', 'hygiene',
        'routine', 'verified', 'dose', 'report', 'passport', 'zoom', 'online'
    ],
    Topic.FOOD: [
        'food', 'dessert', 'Recipe', 'lunch', 'breakfast', 'dinner', 'pasta', 'hamburger', 'cookies', 'cook', 'bake',
        'restaurant', 'meal', 'chef', 'meat', 'hungry', 'starving', 'coffee', 'dishes', 'baking', 'cooking', 'eating',
        'eggs', 'cake', 'rise', 'cheeseburgers', 'pasta', 'fish', 'pizza', 'salad', 'sandwich', 'chocolates', 'ships'
    ],
    Topic.TRAVEL: [
        'Vacation', 'abroad', 'airplane', 'trip', 'country', 'visit', 'journey', 'Israel', 'camping', 'Greece',
        'United States', 'London', 'Canada', 'view', 'river', 'tourism', 'Thailand', 'beach', 'world', 'flight',
        'Italy', 'Dubai', 'Asia', 'travel', 'Europe', 'America', 'Germany', 'Argentina', 'Australia', 'Bulgaria',
        'China', 'Japan', 'France', 'Italy', 'Poland', 'Russia', 'place'
    ]
}


def map_words(words: List[str]) -> Dict[Topic, int]:
    mapping = {}
    for topic, topic_words in TOPIC_WORDS_MAPPING.items():
        mapping[topic] = sum(1 if word.lower() in topic_words else 0 for word in words)

    return mapping
