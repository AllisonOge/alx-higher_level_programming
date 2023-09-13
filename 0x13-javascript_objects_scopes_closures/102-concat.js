#!/usr/bin/node
const fs = require('fs/promises'); // Use fs.promises for promise-based file operations

async function main () {
  const files = [];
  for (let idx = 2; idx < process.argv.length; idx++) {
    files.push(process.argv[idx]);
  }

  try {
    let buffer = '';

    for (let i = 0; i < 2; i++) {
      // Read content of file and append to buffer
      const data = await fs.readFile(files[i], 'utf8');
      buffer += data;
    }

    // Write the concatenated content to the third file
    await fs.writeFile(files[2], buffer, 'utf8');
  } catch (err) {
    console.error(err);
  }
}

main();
