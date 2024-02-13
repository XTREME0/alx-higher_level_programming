#!/usr/bin/node

const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    const chr = c || 'X';
    for (let i = 0; i < this.size; i++) {
      console.log(chr.repeat(5));
    }
  }
}
module.exports = Square;
