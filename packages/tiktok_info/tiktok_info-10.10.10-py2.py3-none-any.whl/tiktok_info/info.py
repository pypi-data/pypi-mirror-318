import requests
import urllib.parse
import re
import argparse
import sys


class TikTokInfo:
    def __init__(self, url):
        self.url = url
        self.final_url = self._get_final_url()
        self.info = self._get_info()
        self.page_source = self._get_page_source()
    
    def _get_final_url(self):
        """Dapatkan URL final setelah redirect."""
        return requests.head(self.url, allow_redirects=True).url
    
    def _get_info(self):
        """Dapatkan informasi dasar video TikTok."""
        api_url = f"https://www.tiktok.com/oembed?url={self.final_url}"
        response = requests.get(api_url)
        if response.status_code != 200:
            raise Exception("Gagal mendapatkan informasi video.")
        return response.json()
    
    def _get_page_source(self):
        """Dapatkan sumber halaman untuk ekstraksi avatar."""
        author = self.info.get('author_unique_id', '')
        response = requests.get(
            f"https://www.tiktok.com/@{author}",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        if response.status_code != 200:
            raise Exception("Gagal mendapatkan sumber halaman pengguna.")
        return response.text
    
    def author(self):
        """Kembalikan nama penulis."""
        return self.info.get('author_name', 'Tidak Diketahui')
    
    def title(self):
        """Kembalikan judul video."""
        return self.info.get('title', 'Tidak Diketahui')
    
    def thumbnail(self):
        """Kembalikan URL thumbnail video."""
        return self.info.get('thumbnail_url', 'Tidak Diketahui')
    
    def avatar(self):
        """Kembalikan URL avatar penulis."""
        match = re.search(
            r'"avatarLarger":"(https:[^"]+)"',
            self.page_source
        )
        if match:
            return match.group(1).replace('\\u002F', '/')
        return 'Tidak Diketahui'
    
    def endpoint(self):
        """Kembalikan URL endpoint final video."""
        return self.final_url


def cli():
    parser = argparse.ArgumentParser(
        description="TikTok Info CLI - Ambil informasi video TikTok langsung dari terminal"
    )
    parser.add_argument("-url", help="URL video TikTok", required=False)
    parser.add_argument("-list", action="store_true", help="Tampilkan semua informasi (author, title, thumbnail, avatar, endpoint)")
    parser.add_argument("-author", action="store_true", help="Tampilkan nama penulis")
    parser.add_argument("-title", action="store_true", help="Tampilkan judul video")
    parser.add_argument("-thumbnail", action="store_true", help="Tampilkan URL thumbnail")
    parser.add_argument("-avatar", action="store_true", help="Tampilkan URL avatar")
    parser.add_argument("-endpoint", action="store_true", help="Tampilkan URL endpoint final")
    parser.add_argument("-help", action="store_true", help="Tampilkan panduan penggunaan")

    args = parser.parse_args()

    if args.help:
        print("""
Panduan Penggunaan tiktok_info:
  -url [URL]       : Masukkan URL video TikTok
  -list            : Tampilkan semua informasi video (author, title, thumbnail, avatar, endpoint)
  -author          : Tampilkan nama penulis video
  -title           : Tampilkan judul video
  -thumbnail       : Tampilkan URL thumbnail video
  -avatar          : Tampilkan URL avatar penulis
  -endpoint        : Tampilkan URL endpoint final video

Contoh:
  tiktok_info -url https://vm.tiktok.com/ZS6F3MQnL/ -list
  tiktok_info -url https://vm.tiktok.com/ZS6F3MQnL/ -avatar
        """)
        sys.exit()

    if not args.url:
        print("Harap masukkan URL video TikTok dengan flag -url")
        sys.exit()

    tiktok = TikTokInfo(args.url)

    if args.list:
        print("Author:", tiktok.author())
        print("Title:", tiktok.title())
        print("Thumbnail:", tiktok.thumbnail())
        print("Avatar:", tiktok.avatar())
        print("Endpoint URL:", tiktok.endpoint())
    if args.author:
        print("Author:", tiktok.author())
    if args.title:
        print("Title:", tiktok.title())
    if args.thumbnail:
        print("Thumbnail:", tiktok.thumbnail())
    if args.avatar:
        print("Avatar:", tiktok.avatar())
    if args.endpoint:
        print("Endpoint URL:", tiktok.endpoint())


if __name__ == "__main__":
    cli()
