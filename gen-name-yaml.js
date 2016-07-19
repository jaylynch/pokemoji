'use strict';

var PokeApi = require('pokeapi');
var api = PokeApi.v1();
var async = require('async');
var jsonfile = require('jsonfile');
var yaml = require('node-yaml');

var jsonOut = './gen1.json';
var yamlOut = './gen1.yaml';
var emojipacksYamlOut = './pokemon-by-name.yaml';

var numbers = [];
var all_gen1 = {};
var calls = [];

for (let i=1; i<152; i++) {
  numbers.push(i);
}

async.eachSeries(numbers, function(i, callback){
  api.get('pokemon', i).then(function(p){
    all_gen1[i] = p;
    console.log('Got ' + i + ': ' + all_gen1[i]['name'] + '!');
    callback();
  }, function(err) {
    console.log('ERROR: ', err);
    callback(err);
  });
}, function(err) {
  if (err) {
    console.log('BIG ERROR: ', err);
  } else {
    console.log('API fetches done!');
  }

  jsonfile.writeFile(jsonOut, all_gen1, {spaces: 2}, function(err){
    if (err) {
      console.error('Error writing JSON output: ', err);
    }
  });

  var yamlObj = {'title': 'pokemon-by-name', 'emojis': []};
  for (let key of Object.keys(all_gen1)) {
    let p = all_gen1[key];
    yamlObj.emojis.push({
      'name': ('' + p['name']).toLowerCase(),
      'src': 'http://127.0.0.1:8000/pokemon-' + key + '.png'
    }); 
  }
  yaml.write(yamlOut, all_gen1, 'utf8', function(err){
    if (err) {
      console.error('Error writing YAML output: ', err);
    }
  });
  yaml.write(emojipacksYamlOut, yamlObj, 'utf8', function(err){
    if (err) {
      console.error('Error writing EmojiPacks YAML output: ', err);
    }
  });
});
