import csv
from pathlib import Path
from typing import Optional

from .auth import get_client


class Process:
    """Process interface for the Metdley API."""

    def __init__(self):
        self._client = None

    def _get_client(self):
        if not self._client:
            self._client = get_client()
        return self._client

    def csv(self, input_file: str, output_file: Optional[str] = None) -> str:
        """
        Process a CSV file through the Metdley API.

        Takes a CSV file containing identifiers (ISRC, UPC, or Artist/Track, Artist/Album pairs)
        and returns enriched metadata from various music services.

        Args:
            input_file (str): Path to the input CSV file
            output_file (str, optional): Path for the output CSV file. If not provided,
                                       creates 'metdley_<input_filename>' in the same directory

        Returns:
            str: Path to the output file containing the enriched data
        """
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")

        if output_file is None:
            output_path = input_path.parent / f"metdley_{input_path.name}"
        else:
            output_path = Path(output_file)

        # Send the CSV file to the API
        client = self._get_client()
        original_content_type = client.headers["Content-Type"]
        client.headers["Content-Type"] = "application/octet-stream"

        try:
            with open(input_path, "rb") as f:
                csv_data = f.read()
                response = client.request(
                    "POST",
                    "/v1/process",
                    body=csv_data,
                )
        finally:
            pass

        # Write the response directly to the output file
        with open(output_path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=response.keys())
            writer.writeheader()
            writer.writerow(response)


# Create instance
process = Process()
