#!/usr/bin/node
const [nodePath, scriptPath, arg1, arg2] = process.argv;
const requiredOutput = '${arg1} is ${arg2}';
console.log(requiredOutput);
