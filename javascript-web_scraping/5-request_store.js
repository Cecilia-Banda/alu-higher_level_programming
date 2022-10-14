#!/usr/bin/node

const fs = require('fs');
const request = require('request');
request(process.argv[2], (error, res, body) => {
  if (error) console.log(error);
  try {
    fs.writeFile(process.argv[3], body, 'utf-8', (err, result) => {
      if (err) console.log(err);
    });
  } catch (error) {
    console.log(error);
  }
});
