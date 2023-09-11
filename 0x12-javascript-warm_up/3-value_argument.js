#!/usr/bin/node
if (process.argv[2] === undefined) console.log('No argument');
else {
  for (let idx = 2; process.argv[idx] !== undefined; idx++) {
    console.log(process.argv[idx]);
  }
}
