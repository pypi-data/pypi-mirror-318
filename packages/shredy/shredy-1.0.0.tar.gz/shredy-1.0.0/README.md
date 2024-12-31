# Git-Based SR&ED Reporting Tool

## Overview

The Git-Based SR&ED Reporting Tool is a CLI tool designed to help Canadian startups using Git generate supporting documents for SR&ED (Scientific Research and Experimental Development). By integrating with GitHub, this tool can also help to identify and validate relevant technical work for SR&ED purposes.

## Key Features

* **GitHub Integration**: Connect your repositories to pull data on authors, branches, and commits.
* **Hierarchical Validation Process**: Select relevant authors, branches, and optional commits to ensure only SR&ED-relevant work is included.
* **PDF Generation**: Export SR&ED-compliant technical write-ups directly as PDFs.

## Installation

The CLI tool is available via pip:

1. Install the tool:
   ```bash
   pip install shredy 
   ```

## Usage

Use the CLI commands to automate report generation directly from your terminal. It will authenticate via the Git authentication manager, make a call to the Github API, and generate a report in PDF files for a specified tax year.

1. Run this line in the terminal:
   ```bash
   shredy [github username] [repo name] [year]
   ```

This will generate SR&ED supporting documentation for every contributor of the repository. It will document the type of commits and the date logs of the commits for each contributor.

If there are more than 3 contributors, a new file for the SR&ED activity logs will be generated.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.

2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```

4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

For support, please open an issue on GitHub or contact shredy.tax@gmail.com.
