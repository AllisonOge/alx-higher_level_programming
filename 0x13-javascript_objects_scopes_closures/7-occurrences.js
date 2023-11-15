#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accumulator, currentValue) => {
    if (currentValue === searchElement) return accumulator + 1;
    else return accumulator;
  }, 0);
};
