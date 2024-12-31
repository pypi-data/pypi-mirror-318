# GCP Secret Manager CLI 

### gcp-secret-manager-cli (0.0.6)
A command-line interface tool for managing secrets in Google Cloud Platform's Secret Manager service with support for bulk operations using environment files.


# Features

1. List Management
   - List all secrets in your GCP project
   - Filter secrets by prefix
   - Display creation timestamps in local timezone

2. Secret Operations
   - Add/update secrets individually
   - Retrieve a single secret value
   - Bulk import from environment files
   - Support for environment prefixes
   
3. Removal Capabilities
   - Delete individual secrets
   - Batch deletion by prefix
   - Force deletion option

4. Rich Terminal Interface
   - Progress indicators
   - Color-coded outputs
   - Operation summaries
   - Interactive confirmations


# Installation

```bash
$ pip install gcp-secret-manager-cli
```

### Prerequisites
- Python >=3.8
- GCP project with Secret Manager API enabled
- Configured GCP credentials


# Configuration

Create a `.env` file in your project root:
```plaintext
PROJECT_ID=your-gcp-project-id  # Required: Your GCP Project ID
TZ=Asia/Taipei                  # Optional: Timezone for timestamps (default: UTC)
```


# Usage

The CLI provides two command aliases:
- `gcp-secrets`: Full command name
- `sm`: Short alias (Secret Manager)

## Command Overview
```bash
❯ sm
🔐 Secret Manager CLI Tool
```

### Environment Settings
Place the following variables in the .env file to reduce the number of commands needed when using the CLI.
| Setting    | Description                                   |
|------------|-----------------------------------------------|
| PROJECT_ID | GCP Project ID for Secret Manager operations |
| TZ         | Timezone for displaying timestamps (default: UTC) |

### Available Commands
| Command      | Description                    |
|--------------|--------------------------------|
| add          | Add secrets from file or command line |
| remove (rm)  | Remove secrets by prefix or key |
| list (ls)    | List all secrets |
| get          | Get single secret |

### Usage Examples

#### Project Configuration
```bash
# If .env file does not have PROJECT_ID configured
$ sm list -P PROJECT_ID                 # Specify PROJECT_ID
```

#### Adding Secrets
```bash
# From environment file
$ sm add -e                             # Add from default .env file
$ sm add -e .env.dev                    # Add from specific env file
$ sm add -e .env.dev -p DEV             # Add with prefix (underscore will be added automatically: DEV_APP_VER)

# Single secret
$ sm add DB_URL "mysql://localhost"     # Add single secret
```

#### Removing Secrets
```bash
# From environment file
$ sm remove -e                          # Remove from default .env file
$ sm remove -e .env.dev                 # Remove from specific env file

# By prefix or key
$ sm remove -p DEV                      # Remove by prefix (underscore will be added automatically)
$ sm remove DB_URL                      # Remove single secret
$ sm rm -f -p TEST                      # Force remove by prefix without confirmation

# Remove all secrets
$ sm rm --all                           # Remove all secrets (⚠️ DANGEROUS)
$ sm rm --all -f                        # Force remove all secrets without confirmation
```

#### Listing Secrets
```bash
$ sm list                               # List all secrets
$ sm list -p DEV                        # List secrets with prefix (underscore will be added automatically)
$ sm ls -p TEST                         # List secrets with prefix (alias)
```

#### Retrieving Secret Value
```bash
$ sm get DB_URL                         # Get single secret value
```

## Command Options
### Global Options
- `-P, --project-id`: Override GCP project ID
- `--version`: Show version

### Add Command
- `-e, --env-file`: Source env file
- `-p, --prefix`: Add prefix to secret names
- `KEY VALUE`: Add single secret

### Remove Command
- `-e, --env-file`: Remove from env file
- `-p, --prefix`: Remove by prefix
- `--all`: Remove all secrets (⚠️ DANGEROUS)
- `-f, --force`: Skip confirmation
- `KEY`: Remove single secret

### List Command
- `-p, --prefix`: Filter secrets by prefix

### Get Command
- `KEY`: Retrieve single secret value


# Development

### Setup
```bash
git clone https://github.com/TaiwanBigdata/gcp-secret-manager-cli.git
cd gcp-secret-manager-cli
python -m venv env
source env/bin/activate  # Linux/Mac
pip install -e .
```


# Dependencies

### Core
- google-api-core>=2.23.0
- google-cloud-secret-manager>=2.21.1
- rich>=13.9.4
- click>=8.1.7
- python-dotenv>=1.0.1


# License

This project is licensed under the MIT License.


# Project Structure

```
gcp-secret-manager-cli/
├── src/
│   └── gcp_secret_manager_cli/
│       ├── core/
│       │   ├── client.py
│       │   └── manager.py
│       ├── utils/
│       │   ├── console.py
│       │   └── env.py
│       ├── __main__.py
│       └── cli.py
├── LICENSE
├── pyproject.toml
├── readgen.toml
├── README.md
└── requirements.txt
```


---
> This document was automatically generated by [ReadGen](https://github.com/TaiwanBigdata/readgen).
