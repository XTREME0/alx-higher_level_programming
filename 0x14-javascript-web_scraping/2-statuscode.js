#!/usr/bin/node

const { argv } = require('process');
const r = require('request');

r.get(argv[2], (err, resp) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + resp.statusCode);
});
