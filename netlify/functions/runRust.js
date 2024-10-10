// netlify/functions/runRust.js
const { exec } = require('child_process');
const path = require('path'); 

exports.handler = async function (event, context) {
  return new Promise((resolve, reject) => {
    // Call the Rust binary with arguments
    exec('./bdat-toolset info file.bdat -t TableName', (error, stdout, stderr) => {
      if (error) {
        console.error('Error executing Rust binary:', error);
        reject({
          statusCode: 500,
          body: 'Error executing Rust binary',
        });
        return;
      }

      console.log('stdout:', stdout);
      resolve({
        statusCode: 200,
        body: stdout || stderr,
      });
    });
  });
};