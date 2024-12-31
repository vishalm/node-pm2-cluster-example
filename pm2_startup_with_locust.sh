#!/bin/bash

# Variables
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

# Function to check and set up Python virtual environment
setup_venv() {
    echo "Checking for virtual environment..."
    if [ ! -d "$VENV_DIR" ]; then
        echo "Virtual environment not found. Setting up virtual environment..."
        python3 -m venv $VENV_DIR
        if [ $? -ne 0 ]; then
            echo "Failed to create virtual environment. Exiting."
            exit 1
        fi
    else
        echo "Virtual environment found."
    fi

    echo "Activating virtual environment..."
    source $VENV_DIR/bin/activate

    echo "Checking for required Python dependencies..."
    if [ -f "$REQUIREMENTS_FILE" ]; then
        pip install --upgrade pip
        pip install -r $REQUIREMENTS_FILE
        if [ $? -ne 0 ]; then
            echo "Failed to install Python dependencies. Exiting."
            exit 1
        fi
    else
        echo "Requirements file not found. Skipping dependency installation."
    fi
}

# Start PM2 apps
start_pm2() {
    echo "Starting PM2 Node.js applications..."
    pm2 start ecosystem.config.js --env production

    if [ $? -ne 0 ]; then
        echo "Failed to start PM2 apps. Exiting."
        exit 1
    fi

    echo "Saving PM2 process list..."
    pm2 save

    echo "Generating PM2 startup script..."
    pm2 startup
}

# Run Locust load tests
run_locust_tests() {
    echo "Starting Locust load testing for the first app in detached mode..."
    locust -f locustfile.py --host=http://localhost:30001 --users 10 --spawn-rate 2 --headless --run-time 5m &

    echo "Starting Locust load testing for the second app in detached mode..."
    locust -f locustfile.py --host=http://localhost:30002 --users 10 --spawn-rate 2 --headless --run-time 5m &
}

# Main script
echo "Starting PM2 and Locust setup..."

# Set up Python virtual environment and install dependencies
setup_venv

# Start PM2 applications
start_pm2

# Run Locust load tests
run_locust_tests

echo "PM2 applications and Locust tests started successfully!"
