# === IMPORTS: BUILT-IN ===
import os

# === IMPORTS: THIRD-PARTY ===

# === IMPORTS: LOCAL ===
from configs.preprocessor_config import PreprocessorConfig


class Preprocessor:
    def __init__(self, config: PreprocessorConfig):
        self.config = config
        os.makedirs(self.config.processed_data_folder, exist_ok=True)

    def step1_foobar(self, data):
        c = self.config
        pass

    def step2_foobar(self, data):
        c = self.config
        pass

    def process(self):
        c = self.config

        # === LOAD DATA
        # TODO: load raw data using the appropriate package
        data = None

        # === EXECUTE THE PREPROCESSING STEPS
        # TODO: implement the preprocessing steps in reasonably-sized functions
        # TODO: optionally, save the output of each preprocessing step
        data = self.step1_foobar(data)
        data = self.step2_foobar(data)
        
        # === SAVE PROCESSED DATA
        # TODO: save processed data using the appropriate package
        processed_data_path = os.path.join(c.processed_data_folder, "final.[INSERT EXTENSION]")


if __name__ == "__main__":
    pass