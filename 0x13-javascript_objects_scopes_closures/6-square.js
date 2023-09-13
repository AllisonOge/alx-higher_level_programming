#!/usr/bin/node
const Square0 = require('./5-square');
class Square extends Square0 {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
