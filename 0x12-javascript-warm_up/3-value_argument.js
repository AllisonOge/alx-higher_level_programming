#!/usr/bin/node
if (process.argv.length <= 2) console.log('No argument');
process.argv.forEach(function (arg, idx) {
  if (idx > 1)  {
    console.log(arg);
  }
});
