FROM nvidia/cuda:12.5.0-devel-ubuntu22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    curl \
    vim \
    git \
    build-essential \
    gcc \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libz-dev \
    libffi-dev \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


ARG USERNAME=shodh
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
WORKDIR /app
COPY . /app

RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip3 install --upgrade pip
RUN pip3 install ollama
RUN pip3 install tqdm
EXPOSE 11434


RUN sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
