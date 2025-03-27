from shared.logging import log

class Planner:
    def __init__(self, memory):
        self.memory = memory

    def get_next_task(self):
        log("[Planner]: Checking for new tasks...")
        task = self.memory.retrieve_latest_request()
        if not task:
            return None
        return {
            "description": task.get("description", "No description"),
            "type": task.get("type", "general"),
            "payload": task.get("payload", {})
        }
