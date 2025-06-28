from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class Config:
    BOT_TOKEN: str

config = Config(
    BOT_TOKEN= os.getenv("BOT_TOKEN")
)