# opt-in telemetry, disabled by default
import os

TELEMETRY_ENABLED = os.getenv('PRAISON_TELEMETRY', 'false').lower() == 'true'

def track_event(event_name: str, metadata: dict = None):
    if not TELEMETRY_ENABLED:
        return
    # anonymous usage stats only
    pass
