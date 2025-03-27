import time
from planner import Planner
from agent_router import AgentRouter
from memory import Memory
from config import settings
from shared.logging import log

class ZaraCore:
    def __init__(self):
        self.memory = Memory()
        self.planner = Planner(self.memory)
        self.router = AgentRouter(self.memory)
        self.status = "Initializing"

    def startup_check(self):
        log("Performing startup checks...")
        self.memory.load()
        self.status = "Online"
        log("Zara is online. Ready to evolve.")

    def run_loop(self):
        self.startup_check()
        while True:
            log("\n[Zara]: What would you like me to build or improve today?")
            task = self.planner.get_next_task()
            if task:
                log(f"[Planner]: Task received: {task['description']}")
                response = self.router.dispatch(task)
                log(f"[Router]: Task result: {response}")
                self.memory.log_task(task, response)
            else:
                log("[Zara]: I'm waiting for input or a new idea to explore.")
            time.sleep(settings.loop_interval)

if __name__ == "__main__":
    zara = ZaraCore()
    zara.run_loop()
