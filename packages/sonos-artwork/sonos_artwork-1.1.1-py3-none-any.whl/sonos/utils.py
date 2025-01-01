from __future__ import annotations

import functools
import logging
import socket
from pathlib import Path
from typing import Any

import requests
import yaml

logging.basicConfig(
    level="INFO",
    format="%(asctime)s %(levelname)s %(filename)s %(message)s",
)
logger = logging.getLogger(__name__)


@functools.cache
def load_config(config_file: str | None = None) -> dict[str, Any] | None:
    filename = (
        config_file
        if config_file
        else Path(__file__).resolve().parent / "etc" / "settings.yaml"
    )
    logger.info("Loading config file from '%s'", filename)
    with open(filename) as stream:
        try:
            settings: dict[str, Any] = yaml.safe_load(stream)
        except yaml.YAMLError:
            logger.exception("Error parsing yaml file: '%s'", filename)
        else:
            return settings
    return None


def get_enabled_zone_names() -> set[str]:
    config = load_config()
    zone_names = [z['name'] for z in config.get('zones', [])]
    return set(get_zone_details(zone_names).keys())


def get_zone_names() -> set[str]:
    return set(get_zone_details().keys())


def get_zone_details(zones: list[str] | None = None) -> dict[str, Any]:
    def is_wanted_zone(zone: str) -> bool:
        return True if not zones else zone in zones

    config = load_config()
    url = f"{config['endpoint']}/zones"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    zones_json = resp.json()
    return {
        zone["roomName"]: zone
        for zone_json in zones_json
        for zone in zone_json["members"]
        if is_wanted_zone(zone["roomName"])
    }


def change_volume(increment: int) -> bool:
    config = load_config()
    for zone in get_enabled_zone_names():
        url_vol_increment: str = f"+{increment}" if increment > 0 else str(increment)
        url = f"""{config['endpoint']}/{zone}/volume/{url_vol_increment}"""
        logger.info(
            "Volume in zone: '%s' changing by %d.  Url is '%s'", zone, increment, url
        )
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        resp_json = resp.json()
        if resp_json['status'] != 'success':
            logger.error("Response was not a success.  Received: %s", resp_json)
            return False
    return True


@functools.cache
def get_hostname(hostname: str) -> str:
    return socket.gethostbyname(hostname)
