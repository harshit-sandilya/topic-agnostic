# Topic-Agnostic Conversational AI

This repository contains the codebase for the research paper titled "Topic-Agnostic Conversational AI" published in IEEE. The project aims to create a conversational AI system that can engage in meaningful and dynamic conversations without being restricted to specific topics.

## Project Structure

The project is organized into the following directories and files:

- **Dockerfile**: Defines the Docker image for the project, including the necessary dependencies and environment setup.
- **run.sh**: Shell script to build and run the Docker container for the project.
- **twoLLM**: Contains the implementation of the two-LLM (Language Model) conversational system.
    - **bot.py**: Defines the Bot class, which simulates a human-like conversational agent.
    - **user.py**: Defines the User class, which simulates a user interacting with the bot.
    - **main.py**: Main script to run the two-LLM conversational system.
- **threeLLM**: Contains the implementation of the three-LLM conversational system.
    - **bot.py**: Defines the Bot class, similar to the one in twoLLM.
    - **user.py**: Defines the User class, similar to the one in twoLLM.
    - **judge.py**: Defines the Judge class, which evaluates the conversation and generates scenarios.
    - **main.py**: Main script to run the three-LLM conversational system.

## Setup and Installation

### Prerequisites

- Docker
- NVIDIA GPU with CUDA support

### Building the Docker Image

To build the Docker image, run the following command:

```sh
./run.sh
```

This script will build the Docker image and run a container with the necessary configurations.

## Running the Conversational AI

### Two-LLM System

To run the two-LLM conversational system, execute the following command inside the Docker container:

```sh
python3 twoLLM/main.py
```

### Three-LLM System

To run the three-LLM conversational system, execute the following command inside the Docker container:

```sh
python3 threeLLM/main.py
```

## Code Overview

### `twoLLM/main.py`

This script initializes the User and Bot classes and simulates a conversation between them. The conversation history is stored and updated, and the results are written to a CSV file.

### `threeLLM/main.py`

This script initializes the User, Bot, and Judge classes. It simulates a conversation between the user and the bot, with the judge evaluating the conversation and generating scenarios if needed. The conversation history and results are written to a CSV file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## References

- [Topic-Agnostic Conversational AI - IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10704625)

For any questions or issues, please contact the project maintainers.