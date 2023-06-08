# === IMPORTS: BUILT-IN ===
from dataclasses import dataclass

# === IMPORTS: THIRD-PARTY ===



@dataclass
class PreprocessorConfig:
    raw_data_filename: str
    processed_data_folder: str