import requests
import urllib.parse
import re

class TikTokInfo:
    def __init__(self, url: str):
        """
        Initialize with a TikTok video URL.
        """
        self.url = url
        self.final_url = self._get_final_url()
        self.info = self._get_video_info()
    
    def _get_final_url(self):
        """
        Get the final URL after redirection.
        """
        return requests.head(self.url, allow_redirects=True).url

    def _get_video_info(self):
        """
        Fetch video information using TikTok oEmbed API.
        """
        response = requests.get(f"https://www.tiktok.com/oembed?url={self.final_url}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch TikTok video information.")
    
    def get_author(self):
        """Return the author's unique ID."""
        return self.info.get('author_name', 'Not found')
    
    def get_title(self):
        """Return the video title."""
        return self.info.get('title', 'Not found')
    
    def get_thumbnail(self):
        """Return the video thumbnail URL."""
        return self.info.get('thumbnail_url', 'Not found')
    
    def get_avatar(self):
        """Return the author's avatar URL."""
        author = self.info.get('author_name')
        if not author:
            return 'Not found'
        
        response = requests.get(
            f"https://www.tiktok.com/@{author}",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        match = re.search(r'"avatarLarger":"(https:[^"]+)"', response.text)
        if match:
            return match.group(1).replace('\\u002F', '/')
        return 'Not found'
    
    def get_endpoint(self):
        """Return the final video URL."""
        return self.final_url
