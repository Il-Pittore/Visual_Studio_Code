const TelegramBot = require('node-telegram-bot-api');

var testo = ['Donkey Kong in cucina scopo Elettra Lamborghini',
    'Donkey Kong in cucina scopo Elettra Lamborghini',
    'Scuola acciughina, horto muso e ditalini',
    'Sborro poi rotolo e srotolo il cazzo di Brontolo'];

const token = '5103401015:AAFksIesWp-IfHLlZuRBCTTq_skydHFOvGE';

const bot = new TelegramBot(token, {
    polling: true
})


//bot.on('message', function (msg) {
//    console.log(msg);
//    var chatId = msg.chat.id;
//    if(msg.text == 'pippo'){
//        bot.sendMessage(chatId, 'sul tavolino');
//    }else if(msg.text == '27'){
//        testo.forEach(i => {
//            bot.sendMessage(chatId, i);
//        }); 
//    }
//    else{
//        bot.sendMessage(chatId, msg.text);
//    }
//});

//comando /echo
bot.onText(/\/echo (.+)/, function (msg, match) {
    console.log("Echo reuqest");
    var chatId = msg.chat.id;
    var data = match[1];
    bot.sendMessage(chatId, data);
});

//comando /greet
bot.onText(/\/greet (.+)/, function (msg, match) {
    var chatId = msg.chat.id;
    var data = "Hello " + match[1];
    bot.sendMessage(chatId, data);
});
