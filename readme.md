Here’s an amazing README for your project:  

---

# Node PM2 Cluster Example

## Overview

This repository demonstrates how to set up a **Node.js application** with PM2 in **cluster mode** for optimal load balancing and scalability. It includes two applications running in separate clusters, leveraging PM2's powerful process management capabilities to ensure reliability and performance.

## Features

- **Cluster Mode**: Scales Node.js applications across multiple CPU cores for high performance.
- **Multiple Applications**: Runs two distinct Node.js APIs as separate clusters.
- **Log Management**: Merges logs for all instances for cleaner and centralized log viewing.
- **Robust Process Management**: PM2 ensures high availability by restarting failed processes automatically.
- **Customizable Configuration**: Easily update the number of instances or enable file watching.

---

## Configuration

The application is managed using a PM2 ecosystem configuration file (`ecosystem.config.js`), which allows you to define how your applications should run. 

Here’s the structure of the PM2 configuration:

```javascript
module.exports = {
    apps: [
      {
        name: 'node-app-observability',                  // Your app's name
        script: './node-app-observability/src/app.js',   // The entry file for your app
        instances: 2,                                    // Number of instances
        exec_mode: 'cluster',                            // Use cluster mode for load balancing
        watch: false,                                    // Disable file watching
        merge_logs: true,                                // Merge logs for all instances
      },
      {
        name: 'node-app-observability-pm2',              // Name of the second API
        script: './node-app-observability-pm2/src/app.js', // The entry file for the second app
        instances: 2,                                    // Number of instances
        exec_mode: 'cluster',                            // Use cluster mode for load balancing
        watch: false,                                    // Disable file watching
        merge_logs: true,                                // Merge logs for all instances
      },
    ],
};
```

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- **Node.js**: v16+ recommended
- **PM2**: Latest version (`npm install -g pm2`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vishalm/node-pm2-cluster-example.git
   cd node-pm2-cluster-example
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the applications using PM2:

   ```bash
   pm2 start ecosystem.config.js
   ```

4. Check the status of your applications:

   ```bash
   pm2 list
   ```

---

## Managing the Applications

### Restart Applications

```bash
pm2 restart ecosystem.config.js
```

### Stop Applications

```bash
pm2 stop ecosystem.config.js
```

### View Logs

```bash
pm2 logs
```

### Monitor Performance

```bash
pm2 monit
```

---

## Project Structure

```plaintext
node-pm2-cluster-example/
│
├── node-app-observability/
│   └── src/
│       └── app.js         # Entry file for the first API
│
├── node-app-observability-pm2/
│   └── src/
│       └── app.js         # Entry file for the second API
│
├── ecosystem.config.js     # PM2 ecosystem configuration file
└── package.json            # Project dependencies
```

---

## Scaling Applications

You can scale the applications horizontally by increasing the number of instances in the `ecosystem.config.js` file. For example, to scale to 8 instances:

```javascript
instances: 8,
```

Apply the changes with:

```bash
pm2 reload ecosystem.config.js
```

---

## Troubleshooting

- **App not starting?** Check logs using `pm2 logs`.
- **Issues with configuration?** Validate your ecosystem file using `pm2 validate ecosystem.config.js`.
- **Need to clear PM2 processes?** Run `pm2 delete all`.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

### Happy Clustering with PM2! 🚀

