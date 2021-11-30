var express = require('express');
var app = express();
var server = app.listen(3000);

app.use(express.static('public'));

var socket = require('socket.io');
var io = socket(server);
io.sockets.on('connection', newConnection);


function newConnection(socket)
{
    console.log('New Connection: ' + socket.id);

    socket.on('text', MessageReceived);

    function MessageReceived(data)
    {
        socket.broadcast.emit('text', data);
    }
}



