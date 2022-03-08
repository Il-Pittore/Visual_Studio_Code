const WebSocket = require('ws');

//const serverAddress = 'ws://127.0.0.1:5000';
const serverAddress = 'wss://zarrilli-antonio-5g.glitch.me/';


const ws = new WebSocket(serverAddress, {
    headers: {
        "User-Agent": "Custom ws client"
    }
});

ws.on('open', function(){
    ws.send("Hello server!");
});

ws.on('message', function(msg){
    console.log("Received msg from the server: " + msg);
})