import os
import re
import sys
import json
from argparse import ArgumentParser
from packaging.version import parse
import subprocess
import pkg_resources
import requests

def parse_requirements_file(file_path):
    """Parse a requirements.txt file and return a dictionary of packages and their specified versions."""
    requirements = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                # Handle editable installs
                if line.startswith("-e "):
                    match = re.search(r'#egg=(.+)', line)
                    if match:
                        package = match.group(1)
                        requirements[package] = ""
                    continue
                # Handle packages with versions
                match = re.match(r"^([a-zA-Z0-9_.-]+)([>=<~!]+[\d.]+)?", line)
                if match:
                    package = match.group(1)
                    version_spec = match.group(2) if match.group(2) else ""
                    requirements[package] = version_spec
    return requirements

def get_latest_version(package_name, cache):
    """Get the latest version of a package from PyPI with caching."""
    if package_name in cache:
        return cache[package_name]
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=10)
        if response.status_code == 200:
            data = response.json()
            latest_version = data['info']['version']
            cache[package_name] = latest_version
            return latest_version
    except Exception as e:
        print(f"Error fetching latest version for {package_name}: {e}")
    return None

def get_package_description(package_name):
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data['info']['summary']
    except Exception as e:
        print(f"Error fetching description for {package_name}: {e}")
    return None

def check_versions(requirements, cache):
    """Check the current environment's packages against the requirements file and PyPI."""
    results = []
    for package, version_spec in requirements.items():
        try:
            installed_version = pkg_resources.get_distribution(package).version
        except pkg_resources.DistributionNotFound:
            installed_version = "Not installed"

        latest_version = get_latest_version(package, cache)

        if latest_version:
            specified_version = version_spec
            results.append((package, specified_version, installed_version, latest_version))
        else:
            results.append((package, version_spec, installed_version, "Could not fetch latest"))
    return results

def upgrade_packages(requirements, verbose, force, exclude=None):
    """Upgrade all packages to their latest version, excluding specified ones."""
    for package in requirements.keys():
        if exclude and package in exclude:
            if verbose:
                print(f"Skipping upgrade for {package} as it's excluded.")
            continue
        try:
            if not force:
                installed_version = pkg_resources.get_distribution(package).version
                latest_version = get_latest_version(package, {})
                parsed_installed = parse(installed_version)
                parsed_latest = parse(latest_version)
                if parsed_installed == parsed_latest:
                    if verbose:
                        print(f"{package} is already up-to-date.")
                    continue

            cmd = [sys.executable, "-m", "pip", "install", "--upgrade", package]
            if verbose:
                print(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error upgrading {package}: {e}")

def resolve_dependencies(verbose):
    """Resolve dependency conflicts using pip."""
    if verbose:
        print("Resolving dependency conflicts...")
    
    try:
        # Check for dependency conflicts
        subprocess.run([sys.executable, "-m", "pip", "check"], check=True)
        if verbose:
            print("No dependency conflicts found.")
    except subprocess.CalledProcessError as e:
        print(f"Dependency conflicts found. Attempting to resolve...")
        
        # Step 1: List all conflicting packages
        conflicting_packages = []
        output = subprocess.check_output([sys.executable, "-m", "pip", "check"]).decode()
        for line in output.split('\n'):
            if line.strip():
                package_info = line.split(' ')
                conflicting_packages.append(package_info[0])
        
        # Step 2: Upgrade each conflicting package one by one
        for package in set(conflicting_packages):
            try:
                if verbose:
                    print(f"Upgrading {package} to resolve conflicts...")
                subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error upgrading {package}: {e}")
        
        # Step 3: Check again for any remaining conflicts
        try:
            subprocess.run([sys.executable, "-m", "pip", "check"], check=True)
            if verbose:
                print("All dependency conflicts resolved.")
        except subprocess.CalledProcessError as e:
            print("Some dependency conflicts still exist. Consider manual resolution.")

def upgrade_pip(verbose):
    """Upgrade pip."""
    if verbose:
        print("Upgrading pip...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)

def write_requirements_file(requirements, output_file, version_type):
    with open(output_file, 'w') as f:
        for package, version_spec in requirements.items():
            description = get_package_description(package)
            if description:
                f.write(f"# {description}\n")
            if version_type == 'exact':
                latest_version = get_latest_version(package, {})
                if latest_version:
                    f.write(f"{package}=={latest_version}\n")
                else:
                    f.write(f"{package}{version_spec}\n")
            elif version_type == 'loose':
                if version_spec and version_spec.startswith('>='):
                    f.write(f"{package}{version_spec}\n")
                else:
                    latest_version = get_latest_version(package, {})
                    if latest_version:
                        f.write(f"{package}>= {latest_version}\n")
                    else:
                        f.write(f"{package}{version_spec}\n")
            else:
                f.write(f"{package}{version_spec}\n")

def check_system_prerequisites():
    try:
        import torch
        print(f"PyTorch version: {torch.__version__}")
        if torch.cuda.is_available():
            print("CUDA is available.")
            print(f"CUDA version: {torch.version.cuda}")
            print(f"GPU name: {torch.cuda.get_device_name(0)}")
        else:
            print("CUDA is not available.")
    except ImportError:
        print("PyTorch is not installed.")

def save_settings(args, filename):
    with open(filename, 'w') as f:
        json.dump(vars(args), f)

def load_settings(filename):
    with open(filename, 'r') as f:
        return json.load(f)

profiles = {
    'ai': [
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'keras',
        'pytorch',
        # Add more AI-related packages
    ],
    'data-science': [
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'scipy',
        # Add more data science packages
    ],
    'web-development': [
        'flask',
        'django',
        'requests',
        'beautifulsoup4',
        # Add more web development packages
    ]
}

def main():
    parser = ArgumentParser(description="Check and manage Python package requirements.")
    parser.add_argument("--file", default="requirements.txt", help="Path to the requirements file.")
    parser.add_argument("--upgrade", action="store_true", help="Upgrade packages to the latest versions.")
    parser.add_argument("--write", action="store_true", help="Write the updated requirements to the file.")
    parser.add_argument("--verbose", action="store_true", help="Output verbose information.")
    parser.add_argument("--dry-run", action="store_true", help="Perform all checks without making changes.")
    parser.add_argument("--output", help="Output file for results in JSON format.")
    parser.add_argument("--version-type", choices=['exact', 'loose'], default='exact',
                        help="Type of version specification to use when writing requirements.")
    parser.add_argument("--force", action="store_true", help="Force upgrade packages even if they are already up to date.")
    parser.add_argument("--exclude", nargs='+', help="Exclude specific packages from being upgraded.")
    parser.add_argument("--resolve", action="store_true", help="Resolve dependency conflicts before upgrading.")
    parser.add_argument("--upgrade-pip", action="store_true", help="Upgrade pip before other operations.")
    parser.add_argument("--settings-config", help="Save current settings to a config file.")
    parser.add_argument("--settings", help="Load settings from a config file.")
    parser.add_argument("--doc", action="store_true", help="Add package descriptions as comments in requirements.txt.")
    parser.add_argument("--profile", choices=['ai', 'data-science', 'web-development'], help="Use predefined profiles for package sets.")
    parser.add_argument("--system", action="store_true", help="Check system and hardware prerequisites for packages.")

    args = parser.parse_args()

    # Handle --settings
    if args.settings:
        settings = load_settings(args.settings)
        args = argparse.Namespace(**settings)

    # Handle --settings-config
    if args.settings_config:
        save_settings(args, args.settings_config)

    # Handle --upgrade-pip
    if args.upgrade_pip:
        upgrade_pip(args.verbose)

    # Handle --resolve
    if args.resolve:
        resolve_dependencies(args.verbose)

    # Handle --profile
    if args.profile:
        packages = profiles[args.profile]
        with open(args.file, 'w') as f:
            for package in packages:
                f.write(f"{package}\n")
        print(f"Requirements file updated with {args.profile} profile.")

    if not os.path.exists(args.file):
        print(f"No requirements file found at {args.file}.")
        sys.exit(1)

    requirements = parse_requirements_file(args.file)
    cache = {}
    results = check_versions(requirements, cache)

    if args.verbose:
        print("\n{:<20} {:<15} {:<15} {:<15}".format("Package", "Specified", "Installed", "Latest"))
        print("=" * 65)
        for package, specified, installed, latest in results:
            print(f"{package:<20} {specified:<15} {installed:<15} {latest:<15}")

    # Summary statistics
    total = len(results)
    up_to_date = sum(1 for _, spec, inst, latest in results if inst != "Not installed" and parse(inst) == parse(latest))
    needs_upgrading = sum(1 for _, spec, inst, latest in results if inst != "Not installed" and parse(inst) < parse(latest))
    not_installed = sum(1 for _, spec, inst, _ in results if inst == "Not installed")

    print("\nSummary:")
    print(f"Total packages: {total}")
    print(f"Up to date: {up_to_date}")
    print(f"Needs upgrading: {needs_upgrading}")
    print(f"Not installed: {not_installed}")

    if args.upgrade and not args.dry_run:
        upgrade_packages(requirements, args.verbose, args.force, exclude=args.exclude)

    if args.write and not args.dry_run:
        write_requirements_file(requirements, args.file, args.version_type)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=4)

    if args.doc:
        write_requirements_file(requirements, args.file, args.version_type)

    if args.system:
        check_system_prerequisites()

if __name__ == "__main__":
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "packaging"])
    except subprocess.CalledProcessError as e:
        print("Error installing required libraries: requests, packaging.")
        sys.exit(1)

    main()