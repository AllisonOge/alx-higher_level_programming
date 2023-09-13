#!/usr/bin/node
const dict = require('./101-data').dict;
const newObj = {};

Object.entries(dict).forEach((entry) => {
  const key = entry[0];
  const value = entry[1];

  if (!newObj[value]) newObj[value] = [];

  newObj[value].push(key);
});

console.log(newObj);
