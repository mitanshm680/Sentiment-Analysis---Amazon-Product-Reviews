'''
import json
import logging
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def read_jsonl_file(filename):
    """Read a JSONL file and yield each JSON object."""
    try:
        with open(filename, "r") as file:
            for line in file:
                yield json.loads(line.strip())
    except FileNotFoundError:
        logger.error(f"File '{filename}' not found. Please check the file path.")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format in file '{filename}'.")
        raise

def write_jsonl_file(filename, data):
    """Write data to a JSONL file."""
    with open(filename, "w") as file:
        for entry in data:
            file.write(json.dumps(entry) + "\n")

def process_reviews_and_metadata(metadata_file, reviews_file, output_file):
    """
    Process JSONL metadata and reviews, merging reviews into metadata where parent_asin matches.
    
    Args:
        metadata_file (str): Path to the metadata JSONL file.
        reviews_file (str): Path to the reviews JSONL file.
        output_file (str): Path to save the updated metadata JSONL file.
    """
    try:
        # Create a dictionary to group reviews by parent_asin
        reviews_dict = {}
        skipped_reviews = 0

        logger.info("Processing reviews...")
        for review in tqdm(read_jsonl_file(reviews_file), desc="Processing Reviews", unit="review"):
            parent_asin = review.get("parent_asin")
            if parent_asin:
                reviews_dict.setdefault(parent_asin, []).append(review)
            else:
                skipped_reviews += 1

        if skipped_reviews > 0:
            logger.warning(f"Skipped {skipped_reviews} reviews missing 'parent_asin'.")

        # Process metadata and merge reviews
        logger.info("Merging reviews into metadata...")
        updated_metadata = []
        matched_metadata = 0
        skipped_metadata = 0

        for metadata in tqdm(read_jsonl_file(metadata_file), desc="Merging Metadata", unit="metadata"):
            parent_asin = metadata.get("parent_asin")
            if parent_asin in reviews_dict:
                metadata["reviews"] = reviews_dict[parent_asin]
                matched_metadata += 1
            else:
                skipped_metadata += 1
            updated_metadata.append(metadata)

        if skipped_metadata > 0:
            logger.warning(f"Skipped {skipped_metadata} metadata items without matching reviews.")
        
        logger.info(f"Matched {matched_metadata} metadata items with reviews.")

        # Save the updated metadata
        write_jsonl_file(output_file, updated_metadata)
        logger.info(f"Updated metadata with reviews saved to '{output_file}'.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

# Usage
if __name__ == "__main__":
    process_reviews_and_metadata("metadata.jsonl", "data.jsonl", "updated_metadata.jsonl")
'''
import json

# Path to your JSONL file
jsonl_file_path = 'updated_metadata.jsonl'

def print_first_element_nicely(jsonl_file_path):
    with open(jsonl_file_path, 'r') as file:
        # Read the first line from the file
        first_line = file.readline()
        # Parse the JSON data
        first_element = json.loads(first_line)
        # Pretty-print the first element
        print(json.dumps(first_element, indent=4))

# Call the function
print_first_element_nicely(jsonl_file_path)
