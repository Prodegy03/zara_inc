from shared.logging import log

class AgentRouter:
    def __init__(self, memory):
        self.memory = memory

    def dispatch(self, task):
        task_type = task.get("type")
        log(f"[Router]: Dispatching task of type '{task_type}'")

        if task_type == "codegen":
            from autocoder.run import handle_codegen
            return handle_codegen(task)
        elif task_type == "light":
            from phi_helper.run import handle_light_task
            return handle_light_task(task)
        else:
            return "[Router]: Unknown task type."
