# TikTokInfo

**TikTokInfo** is a Python library and command-line tool for fetching TikTok video metadata, including the author, title, thumbnail, and avatar.

---

## 📦 **Installation**

```bash
pip install tiktok_info
```
## **run**

run manually using the command:
```
tiktok_info -url <url_tiktok> -help
```
run using the script:
```
from tiktok_info import TikTokInfo

url = "https://vm.tiktok.com/vid_id/"
tiktok = TikTokInfo(url)

print("Author:", tiktok.author())
print("Title:", tiktok.title())
print("Thumbnail:", tiktok.thumbnail())
print("Avatar:", tiktok.avatar())
print("Endpoint URL:", tiktok.endpoint())
