from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # File paths

    AUTHORIZED_FILE: Path = Path(__file__).parent.parent / "resources" / "authorized_targets.txt"
    LOGFILE: Path = Path(__file__).parent.parent / "logs" / "nmap_agent_llm_targets.log"

    # Tools
    NMAP_BIN: str = "nmap"

    # Runtime settings
    RATE_LIMIT_SECONDS: int = 2
    MAX_OUTPUT_CHARS: int = 50000

    # LLM config
    LLM_MODEL: str = "gpt-4o-mini"
    LLM_TIMEOUT: int = 30