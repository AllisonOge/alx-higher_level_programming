#!/usr/bin/node
exports.converter = function (base) {
  return function (n) {
    /* convert n to base and return it as a string */
    return n.toString(base);
  };
};
