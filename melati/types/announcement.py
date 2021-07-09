from dataclasses import dataclass

from melati.types.blockchain_format.sized_bytes import bytes32
from melati.util.hash import std_hash


@dataclass(frozen=True)
class Announcement:
    origin_info: bytes32
    message: bytes

    def name(self) -> bytes32:
        return std_hash(bytes(self.origin_info + self.message))
