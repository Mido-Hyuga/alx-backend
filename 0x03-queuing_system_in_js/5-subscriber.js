const redis = require('redis');

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', function () {console.log('Redis client connected to the server');}).on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.subscribe('holberton school channel');

client.on('message', (ch, message) => {
  if (ch == 'holberton school channel') {  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    console.log(message);
    client.quit();

  }
  else {
    console.log(message);
  }
}
})