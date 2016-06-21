'use strict';

var express = require('express');
var app = express();
console.log('starting express...');

// app.get('/', function (req, res) {
//   res.render('out/index.html');
// });

app.use(express.static('out'))

var port = 3000;
console.log('server.js running express on \nhttp://localhost:' + port + '/ \n');
app.listen(port);