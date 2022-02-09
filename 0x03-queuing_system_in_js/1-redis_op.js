const redis = require('redis');

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', function () {
}).on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err}`);
});
console.log('Redis client connected to the server');

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(err, value) {
    if (err) {
        console.error("error");
    } else {
        console.log(value);
    }
});
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
