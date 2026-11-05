
import time
import secrets
import threading
import uuid

_lock = threading.Lock()
_last_ms = -1
_last_random = 0

_RANDOM_MASK = (1 << 74) - 1
_MAX_TIMESTAMP = (1 << 48) - 1


def uuid7(timestamp=None, nanos=None):
    """
    Generate a UUID version 7 using Python's standard library.

    timestamp: Unix timestamp in seconds (optional)
    nanos: Additional nanoseconds (optional)
    """
    global _last_ms, _last_random

    if timestamp is None:
        if nanos is not None:
            raise ValueError("nanos requires a timestamp")
        current_ns = time.time_ns()
    else:
        current_ns = int(timestamp) * 1_000_000_000
        current_ns += int(nanos or 0)

    timestamp_ms = current_ns // 1_000_000

    if not 0 <= timestamp_ms <= _MAX_TIMESTAMP:
        raise ValueError("Timestamp is outside UUIDv7 range")

    if timestamp is None:
        with _lock:
            if timestamp_ms > _last_ms:
                _last_ms = timestamp_ms
                _last_random = secrets.randbits(74)
            else:
                timestamp_ms = _last_ms
                _last_random += 1

                if _last_random > _RANDOM_MASK:
                    _last_ms += 1
                    _last_random = secrets.randbits(74)
                    timestamp_ms = _last_ms

            random_bits = _last_random
    else:
        random_bits = secrets.randbits(74)

    rand_a = random_bits >> 62
    rand_b = random_bits & ((1 << 62) - 1)

    value = (
        (timestamp_ms << 80)
        | (7 << 76)
        | (rand_a << 64)
        | (2 << 62)
        | rand_b
    )

    return uuid.UUID(int=value)


if __name__ == "__main__":
    first = uuid7()
    second = uuid7()

    print("First UUID:", first)
    print("Second UUID:", second)
    print("Version:", first.version)
    print("Correct UUID type:", isinstance(first, uuid.UUID))
    print("Monotonic:", first.int < second.int)
