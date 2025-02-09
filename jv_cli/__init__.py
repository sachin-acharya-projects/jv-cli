import os
import json
import argparse

CONFIG_DIR = os.environ.get("JV_CONFIG_PATH", os.environ["USERPROFILE"])
CONFIG_FILE = os.path.join(CONFIG_DIR, ".jv-config", "config.json")


# Ensure config directory exists
def ensure_config_dir():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)


def load_config():
    ensure_config_dir()
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}


def save_config(config):
    ensure_config_dir()
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


def set_java_home(version, persist=False):
    config = load_config()
    java_home = config.get(version)

    if not java_home:
        print(f"Java version {version} not found in config.")
        return

    os.environ["JAVA_HOME"] = java_home
    os.environ["PATH"] = f"{java_home}/bin;" + os.environ.get("PATH", "")
    print(f"Set JAVA_HOME to {java_home}")

    if persist:
        os.system(f'setx JAVA_HOME "{java_home}"')
        print("JAVA_HOME has been set permanently.")


def set_default_java(version):
    config = load_config()
    if version not in config:
        print(f"Java version {version} not found.")
        return
    config["default"] = version
    save_config(config)
    print(f"Set Java {version} as default.")


def run_java_command():
    config = load_config()
    default_version = config.get("default")
    if not default_version:
        print("No default Java version set.")
        return
    java_home = config.get(default_version)
    if not java_home:
        print(f"Default Java version {default_version} not found in config.")
        return
    command = f'"{java_home}/bin/java" -version'
    os.system(command)


def add_java_config(version, path):
    config = load_config()
    if version in config:
        confirm = (
            input(
                f"Java version {version} already exists. Do you want to overwrite it? (yes/no): "
            )
            .strip()
            .lower()
        )
        if confirm != "yes":
            print("Operation cancelled.")
            return
    config[version] = path
    save_config(config)
    print(f"Added Java {version} at {path} to config.")


def main():
    parser = argparse.ArgumentParser(description="Java Environment Manager")
    parser.add_argument(
        "-jv", "--java-version", help="Set JAVA_HOME to the specified Java version"
    )
    parser.add_argument(
        "-P", "--persist", action="store_true", help="Make JAVA_HOME change persistent"
    )
    parser.add_argument(
        "-d", "--as-default", help="Set a Java version as default for the app"
    )
    parser.add_argument(
        "-java", action="store_true", help="Run Java using the default version"
    )
    parser.add_argument(
        "--config", nargs=2, metavar=("VERSION", "PATH"), help="Add Java path to config"
    )

    args = parser.parse_args()

    if args.config:
        version, path = args.config
        add_java_config(version, path)

    if args.java_version:
        set_java_home(args.java_version, args.persist)

    if args.as_default:
        set_default_java(args.as_default)

    if args.java:
        run_java_command()


if __name__ == "__main__":
    main()
