# TikTokInfo

**TikTokInfo** is a Python library and command-line tool for fetching TikTok video metadata, including the author, title, thumbnail, and avatar.

---

## 📦 **Installation**
```bash
pip install tiktok_info```
## **run**

run manually using the command:
```bash
tiktok_get -url <url_tiktok> -help```
run using the script:
```bash
from tiktok_get_info import TiktokGetInfo
url = "https://vm.tiktok.com/vid_id/"
tiktok = TiktokGetInfo(url)

print("Author:", tiktok.author())
print("Title:", tiktok.title())
print("Thumbnail:", tiktok.thumbnail())
print("Avatar:", tiktok.avatar())
print("Endpoint URL:", tiktok.endpoint())
