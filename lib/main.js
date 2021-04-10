const mqtt = require('mqtt');

(async () => {
  const client = mqtt.connect(process.env.MQTT_URL, {
    username: process.env.MQTT_USERNAME,
    password: process.env.MQTT_PASSWORD,
  });

  const sensorId = process.env.SENSOR_ID;

  // TODO: WIP

  client.on('connect', () => {
    client.subscribe('presence', function(err) {
      if (!err) {
        client.publish('presence', 'Hello mqtt');
      }
    });
  });

  client.on('message', (topic, message) => {
    // message is Buffer
    console.log(topic, message.toString());
    //client.end();
  });
})();
