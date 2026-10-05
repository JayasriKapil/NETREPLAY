import json

# We'll just define the timelines directly for the simulation
PROFILES = {
    "lift": {
        "name": "lift",
        "desc": "Wi-Fi to 5G handover during a lift ride",
        "duration": 15.0,
        "events": [
            {"time": 0.0, "link": "wifi", "rtt_ms": 40.0, "loss_prob": 0.01},
            {"time": 5.0, "link": "wifi", "rtt_ms": 150.0, "loss_prob": 0.1},
            {"time": 7.0, "link": "none", "rtt_ms": 9999.0, "loss_prob": 1.0}, # Drop
            {"time": 9.0, "link": "5g", "rtt_ms": 2000.0, "loss_prob": 0.2},  # Re-attach
            {"time": 12.0, "link": "5g", "rtt_ms": 60.0, "loss_prob": 0.02}
        ]
    }
}