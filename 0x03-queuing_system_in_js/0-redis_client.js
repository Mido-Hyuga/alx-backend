const redis = require('redis');

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', function () {
}).on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err}`);
});
console.log('Redis client connected to the server');