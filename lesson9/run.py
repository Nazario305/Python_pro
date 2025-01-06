import time
from abc import ABC, abstractmethod


class SocialChannel(ABC):
    def __init__(self, followers: int):
        self.followers = followers

    @abstractmethod
    def post(self, message: str) -> None:
        pass

class YouTubeChannel(SocialChannel):
    def post(self, message: str) -> None:
        print(f"Posting to YouTube: {message} ({self.followers} followers)")

class FacebookChannel(SocialChannel):
    def post(self, message: str) -> None:
        print(f"Posting to Facebook: {message} ({self.followers} followers)")

class TwitterChannel(SocialChannel):
    def post(self, message: str) -> None:
        print(f"Posting to Twitter: {message} ({self.followers} followers)")

class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp

def post_a_message(channel: SocialChannel, message: str) -> None:
    channel.post(message)

def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        for channel in channels:
            if post.timestamp <= time.time():
                post_a_message(channel, post.message)


if __name__ == "__main__":
    youtube = YouTubeChannel(followers=1000)
    facebook = FacebookChannel(followers=500)
    twitter = TwitterChannel(followers=200)

    channels = [youtube, facebook, twitter]

    posts = [
        Post(message="Hello World!", timestamp=int(time.time() - 1)),
        Post(message="Second Post!", timestamp=int(time.time() + 10)),
    ]

    process_schedule(posts, channels)
