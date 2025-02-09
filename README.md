# JV-CLI

## Overview

`jv-cli` is a simple command-line utility for managing Java environment versions. It allows users to set `JAVA_HOME`, make it persistent, configure multiple Java installations, and execute Java commands using a default version.

## Installation

You can install `jv-cli` using pip:

```sh
pip install jv-env-cli
```

## Usage

Run the following command to see available options:

```sh
jv -h
```

### Commands

-   **Set JAVA_HOME to a specific version:**

    ```sh
    jv -jv <version>
    ```

-   **Persist JAVA_HOME change (Windows only):**

    ```sh
    jv -jv <version> -P
    ```

-   **Set a default Java version:**

    ```sh
    jv -d <version>
    ```

-   **Run Java using the default version:**

    ```sh
    jv -java
    ```

-   **Add a Java version to the config:**

    ```sh
    jv --config <version> <path>
    ```

## Configuration

`jv-cli` maintains its configuration in a JSON file located at:

-   Windows: `%USERPROFILE%/.jv-config/config.json`

The configuration file stores Java versions and their corresponding paths.

## Example Usage

1. Add Java versions to the configuration:

    ```sh
    jv --config 11 "C:\Program Files\Java\jdk-11"
    jv --config 17 "C:\Program Files\Java\jdk-17"
    ```

2. Set Java 11 as the default:

    ```sh
    jv -d 11
    ```

3. Switch to Java 17 temporarily:

    ```sh
    jv -jv 17
    ```

4. Run the default Java version:

    ```sh
    jv -java
    ```

## License

MIT License

Copyright (c) [Year] [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
