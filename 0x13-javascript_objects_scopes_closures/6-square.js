#!/usr/bin/node

module.exports = class Square extends require('./4-rectangle') {
  constructor (w) {
    super(w, w);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
