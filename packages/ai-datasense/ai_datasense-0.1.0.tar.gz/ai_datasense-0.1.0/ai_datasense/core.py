import requests
import json

class DataAnalyzer:
    """
    A class to analyze data files using AI APIs.
    """
    def __init__(self, api_provider, api_key, api_url, model):
        """
        Initialize the DataAnalyzer with API configuration.
        """
        self.api_provider = api_provider
        self.api_key = api_key
        self.api_url = api_url
        self.model = model

    def _read_file(self, file_path):
        """
        Read the contents of the given file.
        """
        try:
            if file_path.endswith('.csv') or file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    return file.read()
            elif file_path.endswith('.xlsx'):
                import pandas as pd
                return pd.read_excel(file_path).to_csv()
            elif file_path.endswith('.pdf'):
                from PyPDF2 import PdfReader
                reader = PdfReader(file_path)
                return ''.join([page.extract_text() for page in reader.pages])
            elif file_path.endswith('.docx'):
                import docx
                doc = docx.Document(file_path)
                return '\n'.join([para.text for para in doc.paragraphs])
            else:
                raise ValueError("Unsupported file format.")
        except Exception as e:
            raise ValueError(f"Error reading file: {e}")

    def _send_to_ai(self, prompt, file_content):
        """
        Send data to the AI API for processing.
        """
        payload = {
            "messages": [
                {"role": "user", "content": f"{prompt}\n{file_content}"}
            ],
            "max_tokens": 1000,
            "temperature": 0.7
        }

        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"Other error occurred: {err}"

    def analyze(self, file_paths):
        """
        Analyze one or multiple files using AI.
        """
        results = {}

        for file_path in file_paths:
            print(f"\n📂 Processing file: {file_path}")
            try:
                file_content = self._read_file(file_path)
                prompt = (
                    "Analyze the given data and provide:\n"
                    "- Key insights\n"
                    "- Anomalies\n"
                    "- Visualization recommendations\n"
                )
                analysis_result = self._send_to_ai(prompt, file_content)
                results[file_path] = analysis_result
            except Exception as e:
                results[file_path] = f"Error processing file: {e}"

        return results

    def generate_visualization(self, file_path):
        """
        Generate visualization suggestions using AI.
        """
        try:
            file_content = self._read_file(file_path)
            prompt = (
                "Based on the given data, provide visualization suggestions:\n"
                "- Recommended charts\n"
                "- Key visual insights\n"
            )
            visualization_result = self._send_to_ai(prompt, file_content)
            return visualization_result
        except Exception as e:
            return f"Error generating visualization: {e}"
