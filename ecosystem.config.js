module.exports = {
    apps: [
      {
        name: 'node-app-observability',                  // Your app's name
        script: './node-app-observability/src/app.js',               // The entry file for your app (replace with your app's entry file)
        instances: 2,                     // Number of instances (scale to 8)
        exec_mode: 'cluster',             // Use cluster mode for load balancing
        watch: false,                     // Optional: disable file watching (set to true if needed)
        merge_logs: true,                 // Optional: merge logs for all instances
      },
      {
        name: 'node-app-observability-pm2',                        // Name of the second API
        script: './node-app-observability-pm2/src/app.js',          // The entry file for your app (replace with your app's entry file)
        instances: 2,                     // Number of instances (scale to 8)
        exec_mode: 'cluster',             // Use cluster mode for load balancing
        watch: false,                     // Optional: disable file watching (set to true if needed)
        merge_logs: true,  
      },
    ],
  };