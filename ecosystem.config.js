module.exports = {
    apps: [
      {
        name: 'node-app-observability',                  // Your app's name
        script: './node-app-observability/src/app.js',               // The entry file for your app (replace with your app's entry file)
        exec_mode: 'cluster',  // Use cluster mode for load balancing
        instances: 'max',  // Scale to available CPU cores
        watch: false,  // Disable file watching (set to true if needed)
        merge_logs: true,  // Merge logs from all instances into a single log file
        log_date_format: 'YYYY-MM-DD HH:mm:ss',  // Date format for logs
        output: './logs/out.log',  // Location for stdout logs (normal output)
        error: './logs/error.log',  // Location for stderr logs (error output)
        log_file: './logs/combined.log',  // Optional: combined output file for both stdout and stderr
        max_size: '10M',  // Max log file size before rotating
        retain: 5,  // Number of log files to retain (rotate)
        compress: true,  // Compress log files during rotation
        time: true,  // Include timestamp in the log lines                // Optional: merge logs for all instances
      },
      {
        name: 'node-app-observability-pm2',                        // Name of the second API
        script: './node-app-observability-pm2/src/app.js',          // The entry file for your app (replace with your app's entry file)
        exec_mode: 'cluster',  // Use cluster mode for load balancing
        instances: 'max',  // Scale to available CPU cores
        watch: false,  // Disable file watching (set to true if needed)
        merge_logs: true,  // Merge logs from all instances into a single log file
        log_date_format: 'YYYY-MM-DD HH:mm:ss',  // Date format for logs
        output: './logs/out.log',  // Location for stdout logs (normal output)
        error: './logs/error.log',  // Location for stderr logs (error output)
        log_file: './logs/combined.log',  // Optional: combined output file for both stdout and stderr
        max_size: '10M',  // Max log file size before rotating
        retain: 5,  // Number of log files to retain (rotate)
        compress: true,  // Compress log files during rotation
        time: true,  // Include timestamp in the log lines
      },
    ],
  };