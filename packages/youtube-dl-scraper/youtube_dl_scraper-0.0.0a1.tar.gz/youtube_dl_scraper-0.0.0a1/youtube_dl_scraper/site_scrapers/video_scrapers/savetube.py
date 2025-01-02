import json
import math
import random
import requests
from fake_useragent import UserAgent
from youtube_dl_scraper.core.base_scraper import BaseScraper
from youtube_dl_scraper.core.exceptions import (
    YouTubeDLScraperError,
    ScraperExecutionError,
    VideoNotFoundError,
)


class SaveTube(BaseScraper):

    # meta data
    __name__ = "SaveTube"
    __type__ = "video"
    __host__ = "savetube.su"

    audio_qualities = ["32", "64", "128", "192", "320"]

    headers = {
        "Accept": "application/json",
        "Origin": "https://ytshorts.savetube.me",
        "Referer": "https://ytshorts.savetube.me/",
        "Content-Type": "application/json",
    }

    ua_generator = UserAgent(platforms="pc")

    def generate_cdn(self) -> int:
        return math.floor(random.random() * 11) + 51

    def scrape(self, url: str) -> dict:
        f"""scrape {self.__host__} to get a formatted dictionary of video data"""
        headers = {**self.headers, "User-Agent": self.ua_generator.random}
        payload = json.dumps({"url": url})
        response = requests.post(
            f"https://cdn{self.generate_cdn()}.savetube.su/info",
            data=payload,
            headers=headers,
        )
        if response.status_code != 200:
            raise YouTubeDLScraperError(
                "Error occired fetching video data: invalid response code: {}".format(
                    response.status_code
                )
            )
        data = response.json()
        if not data.get("status") or data.get("message", "") != "200":
            raise VideoNotFoundError("No data found for requested video")
        return self.parse_video_data(data["data"])

    def parse_video_data(self, data: dict) -> dict:
        video_data = {}
        video_data["id"] = data["id"]
        video_data["key"] = data["key"]  # unique to this scraper
        video_data["title"] = data["title"]
        video_data["title_slug"] = data["titleSlug"]
        video_data["watch_url"] = data["url"]
        video_data["duration"] = data["duration"]
        video_data["formatted_duration"] = data["durationLabel"]
        video_data["thumbnail"] = data["thumbnail"]
        thumbnail_formats = data["thumbnail_formats"]  # unique to this scraper
        if len(thumbnail_formats) > 0:
            video_data["jpeg_thumbnail"] = thumbnail_formats[0].get("url")

        # parse stream data (video/audio)
        def get_media(media_type, q):
            cdn = self.generate_cdn
            payload = {
                "downloadType": media_type,
                "quality": int(q),
                "key": video_data["key"],
            }
            api = f"https://cdn{cdn()}.savetube.su/download"
            headers = {
                **self.headers,
                "User-Agent": self.ua_generator.random,
                "Authority": api,
            }
            payload = json.dumps(payload)
            # print(payload)
            response = requests.post(api, data=payload, headers=headers)
            data = response.json()
            # print(data)
            if (
                response.status_code != 200
                or not data.get("status")
                or data.get("message", "") != "200"
            ):
                return
            return data.get("data", {}).get("downloadUrl")

        def get_audio(quality):
            return get_media("audio", quality)

        def get_video(quality):
            return get_media("video", quality)

        streams = {}
        # parse audio
        streams["audio_api"] = get_audio  # this scraper supports variable bitrates
        streams["audio"] = []
        for quality in self.audio_qualities:
            parsed_audio_data = {
                "quality": int(quality),
                "label": f"{quality}kbps",
                "get_url": (lambda q: get_audio(q)),
                "args": [quality],
            }
            streams["audio"].append(parsed_audio_data)
        # parse video
        streams["video"] = []
        for vid_stream in data["video_formats"]:
            # if vid_stream.get("default_selected"): pass i dicided its unessary
            quality = vid_stream.get("quality")
            # print(quality)
            parsed_video_stream = {
                "width": vid_stream.get("width"),
                "height": vid_stream.get("height"),
                "label": f"{quality}p" if quality else None,
                "quality": quality,
                "get_url": (lambda q: vid_stream.get("url") or get_video(q)),
                "args": [quality],
            }
            # print(parsed_video_stream['url']())

            streams["video"].append(parsed_video_stream)

        video_data["streams"] = streams
        return video_data

    def custom_prop(self, obj, data: str):
        obj.jpeg_thumbnail = data["jpeg_thumbnail"]  # custom property for this scraper
        return obj
