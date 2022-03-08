const WebSocket = require('ws');

const PORT = 5000; //127.0.0.1:PORT

const wsServer = new WebSocket.Server({
    port: PORT
});

wsServer.on('connection', function(socket, req) {
    //Atampa quando un client si collega al server
    console.log("A client just connected");
    address = req.socket.remoteAddress.slice(7);
    console.log(address + " " +  req.socket.remotePort);

    socket.on('message', function(msg) {
        //Stampa il messaggio inviato dal client
        console.log("Recived message from client: " + msg);
        //reinvaia il messaggio indietro a chi lo ha mandato
        //socket.send("Take this back: " + msg);4
        //Invia il messagio mandato a tutti i client collegati al server
        wsServer.clients.forEach(function(client) {
            //Invia al cliet il messaggio
            client.send("Someone said:" + msg);
        })
    });
});

console.log( (new Date()) + " Server in listening on port " + PORT);