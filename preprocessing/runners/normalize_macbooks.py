from preprocessing.runners.normalize_category import run_normalizer
from preprocessing.normalizers.macbook_normalizer import normalize_product


run_normalizer(
    raw_folder="data/products/macbooks/raw",
    output_folder="data/products/macbooks/normalized",
    normalizer=normalize_product,
    recursive=True
)