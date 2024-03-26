#!/usr/bin/node

const { argv } = require('process');
const r = require('request');
const link = argv[2];
let count = 0;
r.get(link, (err, resp, pg) => {
  if (err) {
    console.log(err);
    return;
  }
  pg = JSON.parse(pg);
  for (const film in pg.results) {
    if (pg.results[film].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count += 1;
    }
  }
  console.log(count);
});
