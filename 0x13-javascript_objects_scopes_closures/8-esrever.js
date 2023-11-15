#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (const i in list) {
    reversed.unshift(list[i]);
  }
  return reversed;
};
