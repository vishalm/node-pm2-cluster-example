Here’s the updated **README.md**, including a note about adding a minimum of 2 users for Locust testing:

---

# Node PM2 Cluster Example

This repository demonstrates a cluster-based setup using PM2 for scaling Node.js applications and Locust for load testing API endpoints. It is designed for performance monitoring and efficient scaling of Node.js apps in production environments.

## Features
- **PM2 Cluster Mode:** Scales Node.js applications across multiple instances to utilize available CPU cores.
- **Locust Load Testing:** Simulates user traffic to test API endpoints and measure performance.
- **Modular Architecture:** Parent project with submodules for individual applications (`node-app-observability`).

---

## Prerequisites
Ensure you have the following installed:
- [Node.js](https://nodejs.org/) (v14 or later)
- [PM2](https://pm2.keymetrics.io/) (`npm install -g pm2`)
- [Python](https://www.python.org/downloads/) (for Locust)
- [Locust](https://locust.io/) (`pip install locust`)

---

## Getting Started

### 1. Clone the Repository
Clone the main project and initialize submodules:
```bash
git clone https://github.com/vishalm/node-pm2-cluster-example.git
cd node-pm2-cluster-example
git submodule update --init --recursive
```

---

### 2. Configure PM2 Ecosystem
The PM2 ecosystem file is preconfigured to manage two apps:
- `node-app-observability` running on port `30001`
- `node-app-observability-pm2` running on port `30002`

#### Start the Applications
Run the following to start both apps using PM2:
```bash
pm2 start ecosystem.config.js
```

#### Verify Running Applications
Check the status of the applications:
```bash
pm2 status
```

#### Stop or Restart Applications
- Stop: `pm2 stop all`
- Restart: `pm2 restart all`

---

### 3. Load Testing with Locust
**Locust** is used to test the performance of the API endpoints. The `locustfile.py` includes test scenarios for both applications.

#### Run Locust
From the project root, start the Locust web interface:
```bash
locust
```

#### Access the Locust Interface
Open your browser and navigate to `http://localhost:8089`. Configure the test by:
- Entering the **number of users** to simulate (minimum 2 users).
- Setting the **spawn rate** (users per second).
- Specifying the target host:
  - For `node-app-observability`: `http://localhost:30001`
  - For `node-app-observability-pm2`: `http://localhost:30002`

#### Test Scenarios
The following endpoints are tested:
- `/health-check`
- `/about`
- `/`
- `/custom`
- `/actuator/info`
- `/actuator/health`
- `/metrics`

Each request checks for a `200` status code. Failures are logged with the corresponding status code.

#### Example Configuration
For basic testing, you can start Locust with **2 users** and a spawn rate of **1 user per second**:
```bash
locust --users 2 --spawn-rate 1
```

---

## Project Structure
```
node-pm2-cluster-example/
├── ecosystem.config.js          # PM2 ecosystem configuration
├── locustfile.py                # Locust test scenarios
├── node-app-observability/      # Submodule for the first app
└── node-app-observability-pm2/  # Submodule for the second app
```

## PM2 Startup with Locust for Load Testing

This script allows you to set up a **Python virtual environment**, install dependencies, start your Node.js applications using **PM2**, and run **Locust load tests** to monitor the performance of your applications.

### Prerequisites:
Before using the script, ensure that you have the following installed:
1. **Python 3** and `pip`
2. **PM2** (for managing Node.js applications)
3. **Locust** (for load testing)
4. **Node.js** and your application setup
5. **requirements.txt** in your repository for Python dependencies

### Usage:
* Run the script to start PM2 and Locust:
   ```bash
   ./pm2_startup_with_locust.sh
   ```

### What the Script Does:

1. **Virtual Environment Setup:**
   - If a Python virtual environment (`venv/`) does not exist, it creates one using `python3 -m venv`.
   - Installs the Python dependencies from `requirements.txt`.

2. **PM2 Setup:**
   - Starts your Node.js applications using PM2 with `ecosystem.config.js`.
   - Saves the PM2 process list and sets up the PM2 startup script to ensure apps restart on system reboots.

3. **Locust Load Testing:**
   - Runs Locust tests for both applications in **headless mode** to simulate user load and monitor their performance.
   - The tests will run for a specified duration (5 minutes) with 10 users and a spawn rate of 2 users per second.

### Notes:

- Make sure the `ecosystem.config.js` file is correctly configured for your PM2 apps.
- You can customize the Locust test parameters (e.g., `--users`, `--spawn-rate`, `--run-time`) in the script as per your load testing requirements.
```

### Steps Breakdown:
1. **Make the script executable**: This step is required to allow the shell script to run with the correct permissions.
2. **Run the script**: The script handles the setup of your environment, starting PM2 applications, and launching Locust tests.




## Metrics & Observability
- **PM2 Logs:** View logs for each application using:
  ```bash
  pm2 logs
  pm2 monit
  ```
- **Locust Reports:** Monitor performance metrics such as response times, throughput, and errors in the Locust web interface.

---

## Contributing
Feel free to fork this repository, submit issues, or create pull requests to enhance the functionality.

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

This README now includes explicit instructions to use **a minimum of 2 users** in the Locust tests to ensure proper load testing and configuration details.