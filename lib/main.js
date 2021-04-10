const fs = require('fs');

const Jimp = require('jimp');
const mqtt = require('mqtt');

const ledSize = 8;

const imgDefault = [];
for (let i = 0; i < ledSize; i++) {
  for (let j = 0; j < ledSize; j++) {
    imgDefault.push([0, 0, 0]);
  }
}

const readLedState = async (id) => {

  // Fix id for better safety
  id = id.replace(/[^a-zA-Z0-9_\-\/]+/g, ' ');

  const path = `./led/${id}.png`;

  if (!fs.existsSync(path)) {
    console.error(`ERROR: Invalid id '${id}'!`);

    return imgDefault;
  }

  const img = await Jimp.read(path);

  if (img.bitmap.width !== ledSize || img.bitmap.height !== ledSize) {
    console.error(`ERROR: Invalid image size ${img.bitmap.width}x${img.bitmap.height}!`);

    return imgDefault;
  }

  const imgData = img.bitmap.data;
  const pixelSize = imgData.length / (ledSize * ledSize);

  const result = [];

  for (let i = 0; i < imgData.length; i += pixelSize) {
    result.push([imgData[i], imgData[i + 1], imgData[i + 2]]);
  }

  return result;
};

(async () => {
  const client = mqtt.connect(process.env.MQTT_URL, {
    username: process.env.MQTT_USERNAME,
    password: process.env.MQTT_PASSWORD,
  });

  const sensorId = process.env.SENSOR_ID;

  const topicState = `${sensorId}/state`
  const topicLed = `${sensorId}/led`

  client.on('connect', () => {
    client.subscribe(topicLed, (err) => {
      if (err) {
        console.error(`ERROR`, err);

        return;
      }

      client.publish(topicState, 'ready');
    });
  });

  client.on('message', (topic, message) => {
    switch (topic) {
      case topicLed:
        readLedState(message.toString()).then(pixelArray => {
          console.log('TODO', pixelArray.length);

          // TODO: send led pixel
        }).catch(err => {
          console.error(`ERROR`, err);
        });

        return;
    }
  });
})();
