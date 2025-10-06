import yaml
from pathlib import Path

class LabelConverter:
    """
    A utility class to convert .labels text files into YAML files
    containing class names for YOLO or similar models.
    """

    def __init__(self, input_file: str, output_file: str):
        self.input_path = Path(input_file)
        self.output_path = Path(output_file)

    def _read_labels(self):
        """Read and clean label names from the input file."""
        if not self.input_path.exists():
            raise FileNotFoundError(f"❌ Input file not found: {self.input_path}")

        with self.input_path.open('r', encoding='utf-8') as file:
            labels = [line.strip() for line in file if line.strip()]
        
        if not labels:
            raise ValueError("⚠️ No valid labels found in the input file.")
        
        return labels

    def _write_yaml(self, labels):
        """Write labels to a YAML file."""
        data = {'names': labels}

        with self.output_path.open('w', encoding='utf-8') as file:
            yaml.safe_dump(data, file, sort_keys=False, allow_unicode=True)

    def convert(self):
        """Main method to perform conversion."""
        labels = self._read_labels()
        self._write_yaml(labels)
        print(f"✅ Successfully converted {len(labels)} labels to '{self.output_path.name}'")

# ------------------------------------------------------------------

if __name__ == "__main__":
    # Imaginary file paths (for demo)
    input_file = r"items.labels"
    output_file = r"items.yaml"

    converter = LabelConverter(input_file, output_file)
    converter.convert()
