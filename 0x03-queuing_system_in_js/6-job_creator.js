const kue = require('kue')

const queue = kue.createQueue();

const job = {
  phoneNumber: 'string',
  message: 'string'
}
const push_notification_code = queue.create('push_notification_code', job).save( function(err){
if( !err ) console.log(`Notification job created: ${push_notification_code.id}`);
});

push_notification_code.on('complete', () => {
  console.log('Notification job completed');

}).on('failed', () => {
  console.log('Notification job failed')
});
