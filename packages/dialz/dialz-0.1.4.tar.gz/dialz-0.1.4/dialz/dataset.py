import json
import os

from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv
from transformers import AutoTokenizer

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

@dataclass
class DatasetEntry:
    """
    Represents a single entry in the dataset, consisting of a positive
    and a negative example.
    """

    positive: str
    negative: str


class Dataset:
    """
    A class to manage a dataset of positive and negative examples.
    """

    def __init__(self):
        """
        Initializes an empty dataset.
        """
        self.entries: List[DatasetEntry] = []

    def add_entry(self, positive: str, negative: str) -> None:
        """
        Adds a new DatasetEntry to the dataset.

        Args:
            positive (str): The positive example.
            negative (str): The negative example.
        """
        self.entries.append(DatasetEntry(positive=positive, negative=negative))

    def add_from_saved(self, saved_entries: List[dict]) -> None:
        """
        Adds entries from a pre-saved dataset.

        Args:
            saved_entries (List[dict]): A list of dictionaries, each containing
                                        "positive" and "negative" keys.
        """
        for entry in saved_entries:
            if "positive" in entry and "negative" in entry:
                self.add_entry(entry["positive"], entry["negative"])
            else:
                raise ValueError(
                    "Each entry must have 'positive' and \
                                 'negative' keys."
                )

    def view_dataset(self) -> List[DatasetEntry]:
        """
        Returns the current dataset as a list of DatasetEntry objects.

        Returns:
            List[DatasetEntry]: The list of all entries in the dataset.
        """
        return self.entries

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the dataset to a JSON file.

        Args:
            file_path (str): The path to the file where the dataset will be \
                saved.
        """
        with open(file_path, "w") as file:
            json.dump([entry.__dict__ for entry in self.entries], file, indent=4)

    @classmethod
    def create_dataset(cls, model_name: str, items: list):
        tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)

        def render_messages(content1, content2):
            messages = [
                {"role": "system", "content": f"Act as if you are extremely {content1}."},
                {"role": "user", "content": content2},
            ]
            return messages

        file_path = os.path.join(os.path.dirname(__file__), "corpus", "prompt_variations.json")

        with open(file_path, "r") as file:
            variations = json.load(file)

        dataset = Dataset()

        for variation in variations:
            # Render positive and negative messages
            positive_message = render_messages(items[0], variation)
            negative_message = render_messages(items[1], variation)

            # Apply the chat template for both
            tokenized_positive = tokenizer.apply_chat_template(positive_message, tokenize=True, add_generation_prompt=True, return_tensors="pt")
            tokenized_negative = tokenizer.apply_chat_template(negative_message, tokenize=True, add_generation_prompt=True, return_tensors="pt")

            # Decode tokenized results
            positive_decoded = tokenizer.decode(tokenized_positive[0])
            negative_decoded = tokenizer.decode(tokenized_negative[0])

            # Add to dataset
            dataset.add_entry(positive_decoded, negative_decoded)

        return dataset

    @classmethod
    def load_from_file(cls, file_path: str) -> "Dataset":
        """
        Loads a dataset from a JSON file.

        Args:
            file_path (str): The path to the JSON file containing the dataset.

        Returns:
            Dataset: A new Dataset instance loaded from the file.
        """
        with open(file_path, "r") as file:
            data = json.load(file)
        dataset = cls()
        dataset.add_from_saved(data)
        return dataset

    @classmethod
    def load_corpus(cls, name: str) -> "Dataset":
        """
        Loads a default pre-saved corpus included in the package.

        Args:
            name (str): The name of the pre-saved corpus to load.

        Returns:
            Dataset: A new Dataset instance with the default corpus.

        Raises:
            FileNotFoundError: If the specified corpus does not exist.
        """

        base_path = os.path.join(os.path.dirname(__file__), "corpus")
        file_path = os.path.join(base_path, f"{name}.json")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Corpus '{name}' not found.")

        return cls.load_from_file(file_path)

    def __str__(self) -> str:
        """
        Returns a string representation of the dataset for easy viewing.
        """
        return "\n".join(
            [
                f"Positive: {entry.positive}, Negative: {entry.negative}"
                for entry in self.entries
            ]
        )
