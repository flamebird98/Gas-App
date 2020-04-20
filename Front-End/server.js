//Load express module with `require` directive
var express = require('express')
var app = express()
var path = require("path")
var http = require('http');
//Define request response in root URL (/)
app.use(express.static('public'));
app.use("/css", express.static(path.join(__dirname, 'public/css')));
app.get('/', function (req, res) {

 //res.sendFile(path.join(__dirname+'/index.html'));
});
//Launch listening server on port 5000
app.listen(5000, function () {
  console.log('app listening on port 5000!')
})