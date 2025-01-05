# reqs-checker

## Overview

`reqs-checker` is a Python tool designed to automate the process of checking the versions of Python packages listed in a `requirements.txt` file against the installed versions in the current environment and the latest versions available on PyPI. This tool ensures compatibility, rapidly accelerates programming, and helps maintain an up-to-date and secure Python environment.

## Features

- **Parse Multiple Requirements Files:** Automatically reads and parses package specifications from one or more `requirements.txt` files.
- **Compare Installed Versions:** Checks the installed version of each package in the environment.
- **Fetch Latest Versions:** Retrieves the latest available version of each package from PyPI.
- **Detailed Compatibility Checks:** Highlights discrepancies and updates needed for each package.
- **Command-Line Tool:** Provides an easy-to-use CLI for quick execution.
- **Custom Upgrades:** Specify a version to upgrade to or force upgrades even if up-to-date.

## Installation

### Install via `pip` (Recommended)

You can install the tool directly from PyPI:

```bash
pip install reqs-checker
```

### Manual Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BenevolenceMessiah/reqs-checker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd reqs-checker
   ```

3. Install the package (this method will install extra unneeded dependencies for the end-user because it contains all the necessary packages for the self-publishing GitHub workflows mechanic. You can comment out lines 4-6):

   ```bash
   pip install .
   ```

## Usage

### Command-Line Interface

After installation, you can run the tool directly from the terminal:

```bash
reqs-checker
```

This will:

1. Parse the `requirements.txt` file in the current directory.
2. Check each package's version (installed, specified, and latest).
3. Display a detailed report in the terminal.

### Command-Line Arguments

| Argument           | Description                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| `--file`           | Path to the `requirements.txt` file (default: `requirements.txt`).                            |
| `--upgrade`        | Upgrade packages to their latest versions.                                                    |
| `--write`          | Write updated versions back to the `requirements.txt` file.                                    |
| `--verbose`        | Output detailed information about each step.                                                   |
| `--dry-run`        | Perform checks without making changes.                                                         |
| `--output`         | Save the results to a file in JSON format.                                                     |
| `--version-type`   | Specify the type of version specification to use when writing requirements (`exact` or `loose`). |
| `--force`          | Force upgrade packages even if they are already up to date.                                    |
| `--exclude`        | Exclude specific packages from being upgraded.                                                 |
| `--resolve`        | Resolve dependency conflicts before upgrading.                                                  |
| `--upgrade-pip`    | Upgrade pip before other operations.                                                            |
| `--settings-config`| Save current settings to a config file.                                                         |
| `--settings`       | Load settings from a config file.                                                               |
| `--doc`            | Add package descriptions as comments in requirements.txt.                                      |
| `--profile`        | Use predefined profiles for package sets (`ai`, `data-science`, `web-development`).           |
| `--system`         | Check system and hardware prerequisites for packages.                                          |

### Output Format

The output displays a table with the following columns:

- **Package:** The name of the package.
- **Specified:** The version specified in `requirements.txt` (if any).
- **Installed:** The version currently installed in the environment.
- **Latest:** The latest version available on PyPI.

Example Output:

```bash
Package              Specified       Installed       Latest         
===================================================================
requests             >=2.28.0       2.28.1          2.31.0         
packaging            >=21.0         22.0            23.0           
pkg_resources        Not specified  0.0.0           Could not fetch
```

## How It Works

### Compatibility Check

The script evaluates compatibility by comparing:

1. **Specified Version**: Extracted from the `requirements.txt` file (e.g., `>=`, `<=`, `==`).
2. **Installed Version**: Retrieved using `pkg_resources.get_distribution`.
3. **Latest Version**: Queried from PyPI via the PyPI JSON API.

For each package, the tool checks if the installed version satisfies the specified constraints and whether it matches the latest version available.

### Core Functions

1. **`parse_requirements_file`:** Reads and parses the `requirements.txt` file.
2. **`get_latest_version`:** Fetches the latest version of a package from PyPI.
3. **`check_versions`:** Compares specified, installed, and latest versions for each package.
4. **`upgrade_packages`:** Handles upgrading packages, with optional forcing or version-specific upgrades.
5. **`main`:** Executes the entire workflow and displays results in a tabular format.

## Contributing

We welcome contributions! Feel free to open issues or submit pull requests to enhance functionality, fix bugs, or improve documentation.

### Future Development

- **Persistent Cache:** A cache mechanism is implemented to store package versions, reducing redundant API calls and improving performance.
- **Multiple Requirements Files:** The tool now supports processing multiple `requirements.txt` files, merging their contents for comprehensive checks.
- **Additional Output Formats:** Results can be exported in JSON or CSV formats, providing flexibility in how the data is used and shared.
- **Pre-release Versions:** Users can choose to include pre-release versions when checking for the latest package versions, offering more granularity in version selection.
- **Parallel Processing:** By utilizing multithreading, the tool fetches package versions concurrently, significantly speeding up the process for large requirement files.
- **Colorized Output:** Terminal output is color-coded to quickly identify packages that are up-to-date, need updating, or are not installed.
- **Progress Indicator:** A progress bar is displayed when fetching versions, enhancing user experience, especially in verbose mode.
- **Config File Support:** Settings can be saved and loaded from JSON config files, allowing users to reuse common sets of options efficiently.
- **Interactive Mode:** Users can interactively decide whether to upgrade each package, providing more control over the upgrade process.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions or suggestions, please reach out to:

- **Email:** ``benevolence.messiah@gmail.com``
- **GitHub:** [BenevolenceMessiah](https://github.com/BenevolenceMessiah)
