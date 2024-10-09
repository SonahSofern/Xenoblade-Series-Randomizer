// netlify/functions/runRust.js
const { exec } = require('child_process');

exports.handler = async function(event, context) {
    console.log("ITS ALIVE!!!");
    console.log('Current working directory:', __dirname);
  return new Promise((resolve, reject) => {
    exec('../../linuxBDAT', (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing Rust binary: ${error}`);
        return reject({
          statusCode: 500,
          body: 'Server Error'
        });
      }

      resolve({
        statusCode: 200,
        body: stdout,
      });
    });
  });
};