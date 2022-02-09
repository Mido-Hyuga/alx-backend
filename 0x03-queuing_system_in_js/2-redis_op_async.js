const redis = require('redis');
const util = require('util');

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => {
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
console.log('Redis client connected to the server');

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const getAsync = util.promisify(client.get).bind(client);
  console.log(await getAsync(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
