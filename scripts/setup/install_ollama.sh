#!/bin/bash
# Script to install Ollama

echo "Installing Ollama..."

# Check if Ollama is already installed
if command -v ollama &> /dev/null; then
    echo "Ollama is already installed."
    exit 0
fi

# Download and install Ollama
echo "Downloading Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# Verify installation
echo "Verifying Ollama installation..."
if command -v ollama &> /dev/null; then
    echo "Ollama installed successfully!"
else
    echo "Failed to install Ollama."
    exit 1
fi

# Start Ollama service
echo "Starting Ollama service..."
ollama serve &

echo "Ollama is ready to use."