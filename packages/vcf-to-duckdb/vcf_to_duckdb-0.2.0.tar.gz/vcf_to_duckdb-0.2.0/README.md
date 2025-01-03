VCF to DuckDB Converter
---

A module tool for converting a VCF (Variant Call Format) file to a DuckDB database (exported as Parquet files and accompanying SQL schema). 

## Features

- Efficient multithreaded batch processing for large files
- Infers data types from VCF headers
- Parses and separates data in compound INFO fields (e.g. from VEP, SnpEFF, etc.)
- URL-decodes specified fields and detects fields still needing decoding 

## Installation

1. Install the required system dependencies:
    - [pyenv](https://github.com/pyenv/pyenv)
    - [Poetry](https://python-poetry.org/)
    - [bcftools](https://samtools.github.io/bcftools/bcftools.html)

2. Install the required Python version (developed with 3.12.3, but other 3.12+ versions should work):
   ```shell
   pyenv install "$(cat .python-version)"
   ```

3. Confirm that `python` maps to the correct version:
   ```
   python --version
   ```

4. Set the Poetry interpreter and install the Python dependencies:
   ```shell
   poetry env use "$(pyenv which python)"
   poetry install
   ```

A `requirements.txt` file is also available and kept in sync with Poetry dependencies in case you don't want to use Poetry, or you can use arret via docker: `docker pull dmccabe606/arret:latest`.

## Usage

```python
from pathlib import Path
from vcf_to_duckdb.convert_utils import convert
Convert a VCF file to DuckDB
convert(
vcf_path=Path("input.vcf.gz"),
db_path=Path("output.db"),
parquet_dir_path=Path("output_parquet"),
multiallelics=True,
compound_info_fields={"CSQ"},
url_encoded_col_name_regexes=["field_."]
)

## Database Schema

The converter creates the following main tables:

### variants
- `vid`: Unique variant identifier (Primary Key)
- `chrom`: Chromosome
- `pos`: Position
- `id`: Variant identifier
- `ref`: Reference allele
- `alt`: Alternative allele
- `qual`: Quality score
- `filters`: Filter array

### vals_info
- `vid`: Variant identifier (Foreign Key)
- `kind`: Field type ('value' or 'info')
- `k`: Field key
- Various value columns for different data types:
  - `v_boolean`, `v_varchar`, `v_integer`, `v_float`, `v_json`
  - Array versions: `v_boolean_arr`, `v_varchar_arr`, etc.

## Data Type Handling

The converter automatically maps VCF data types to appropriate DuckDB types:
- Integer → INTEGER
- Float → FLOAT
- String → VARCHAR
- Character → VARCHAR
- Flag → BOOLEAN

Compound fields (like CSQ) are stored as JSON objects.

## Batch Processing

For large VCF files, the converter processes data in batches (default 100,000 variants per batch) to manage memory usage efficiently.

## URL Decoding

The tool can automatically URL-decode specified columns based on regular expressions matching column names. This is useful for fields containing URL-encoded data.
