# This module handles target specifications for the application.
from .config import Settings


settings = Settings()
class TargetManager:
    def __init__(self, target: str, settings: Settings = settings):
        self.target = target
        self.settings = settings

    def get_target(self) -> str:
        """
        Returns the target if it is authorized.
        Raises FileNotFoundError if authorized file is missing.
        Raises ValueError if the target is not authorized.
        """
        file_path = self.settings.AUTHORIZED_FILE

        try:
            lines = {
                line.strip()
                for line in file_path.read_text().splitlines()
                if line.strip() and not line.strip().startswith("#")
            }
        except FileNotFoundError:
            raise FileNotFoundError(f"Authorized targets file '{file_path}' not found.")

        if self.target not in lines:
            raise ValueError(f"Target '{self.target}' is not authorized.")

        return self.target