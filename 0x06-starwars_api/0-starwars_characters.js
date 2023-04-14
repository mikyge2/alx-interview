#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieurl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let chars = [];
const charNames = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(movieurl, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      chars = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (chars.length > 0) {
    for (const p of chars) {
      await new Promise(resolve => request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          charNames.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: No characters found');
  }
};

const listCharacters = async () => {
  await requestCharacters();
  await requestNames();

  for (const n of charNames) {
    if (n === charNames[charNames.length - 1]) {
      process.stdout.write(n);
    } else {
      process.stdout.write(n + '\n');
    }
  }
};

listCharacters();
