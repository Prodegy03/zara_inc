class Settings:
    def __init__(self):
        # How often Zara checks for tasks (in seconds)
        self.loop_interval = 5

        # Paths for memory and logs
        self.memory_path = "volumes/memory/zara_memory.json"
        self.project_path = "volumes/zara_project/"

        # Default model settings (can be expanded later)
        self.model_temperature = 0.7
        self.max_tokens = 1024

        # Voice config (optional future use)
        self.voice_enabled = True
        self.default_voice = "zara_soft"

settings = Settings()
