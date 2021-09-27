from typing import Text
from hashlib import md5, sha1

import logging

logger = logging.getLogger(__name__)


def get_latest_parse_data_language(all_events):
    events = reversed(all_events)
    try:
        while True:
            event = next(events)
            if (
                event["event"] == "user"
                and "parse_data" in event
                and "language" in event["parse_data"]
            ):
                return event["parse_data"]["language"]

    except StopIteration:
        return None

def is_story_file(file_path: Text) -> bool:
    """Checks if a file is a Rasa story file.

    Args:
        file_path: Path of the file which should be checked.

    Returns:
        `True` if it's a story file, otherwise `False`.
    """
    from rasa.shared.core.training_data.story_reader.yaml_story_reader import (
        YAMLStoryReader,
    )

    return YAMLStoryReader.is_stories_file(
        file_path
    )

def get_file_hash(path: Text) -> Text:
    """Calculate the md5 hash of a file."""
    return md5(file_as_bytes(path)).hexdigest()  # nosec

def file_as_bytes(path: Text) -> bytes:
    """Read in a file as a byte array."""
    with open(path, "rb") as f:
        return f.read()
