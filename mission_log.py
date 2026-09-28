"""
Mission Log & Reporting Module
================================
Functional Module 3.
It records every calculation that user runs, keeps it to a JSON file so
history is saved between sessions, it also prints a summary of analytics report
Input:  calculation name + the inputs/outputs dict for that run
Output: mission_history.json on disk, and a printed report on request
"""
import json
import os
from datetime import datetime
HISTORY_FILE = "mission_history.json"
class MissionLog:
    def __init__(self, history_file: str = HISTORY_FILE):
        self.history_file = history_file
        self.entries = self._load()
    def _load(self) -> list:
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return []
        return []
    def _save(self) -> None:
        with open(self.history_file, "w") as f:
            json.dump(self.entries, f, indent=2)
    def record(self, calculation: str, inputs: dict, outputs: dict) -> None:
        entry = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "calculation": calculation,
            "inputs": inputs,
            "outputs": outputs,}
        self.entries.append(entry)
        self._save()
    def print_report(self) -> None:
        print("\n" + "=" * 45 + "MISSION REPORT" + "=" * 45)
        if not self.entries:
            print("No calculations have been run yet.")
            return
        counts = {}
        for entry in self.entries:
            counts[entry["calculation"]] = counts.get(entry["calculation"], 0) + 1
        print(f"Total calculations run: {len(self.entries)}\n")
        print("By type:")
        for calc_type, count in counts.items():
            print(f"  - {calc_type}: {count}")
        print("\nMost recent calculations:")
        for entry in self.entries[-5:]:
            print(
                f"  [{entry['timestamp']}] {entry['calculation']} "
                f"-> inputs={entry['inputs']}, outputs={entry['outputs']}")