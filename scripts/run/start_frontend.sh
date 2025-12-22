#!/bin/bash
# Script to start the frontend

echo "Starting frontend..."

# Navigate to frontend directory
cd frontend || { echo "Failed to navigate to frontend directory"; exit 1; }

# Install dependencies if not already installed
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install
fi

# Start React development server
echo "Starting React development server..."
npm start

echo "Frontend is running on http://localhost:3000"