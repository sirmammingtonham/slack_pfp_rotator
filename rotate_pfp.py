import os
from slack_sdk import WebClient
from pathlib import Path
import datetime

# Load your token from an env var
SLACK_TOKEN = os.environ["SLACK_USER_TOKEN"]
client = WebClient(token=SLACK_TOKEN)

# Point this at a folder of pre-prepared square images
IMAGES_DIR = Path("./squiddy")
START_OFFSET = 20  # restarted on jul 20th to frame 85


def set_daily_avatar():
    # Pick today’s image (e.g. based on day-of-year)
    images = sorted(IMAGES_DIR.glob("*.png"))
    today = datetime.date.today()
    day_count = today.toordinal() - datetime.date(1970, 1, 1).toordinal()
    idx = (day_count + START_OFFSET) % len(images)
    img_path = images[idx]

    with img_path.open("rb") as img:
        client.users_setPhoto(image=img)
    print(f"Set avatar to {img_path.name!r}")


if __name__ == "__main__":
    set_daily_avatar()
