module.exports = {
  apps: [{
    name: 'sensehat-mqtt-proxy',
    script: './index.js',
    watch: ['lib'],
    watch_delay: 1000,
  }],
};
