#!/usr/bin/node

const { argv } = require('process');
const r = require('request');
const link = 'https://swapi-api.alx-tools.com/api/films/';
r.get(link + argv[2], (err, resp, pg) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(pg).title);
});
