var express = require('express');
var app = express();
var logger = require('morgan');
var bodyParser = require('body-parser');

app.use(express.static('public'));
app.set('view engine','ejs');
app.use(logger('dev'))
app.use(bodyParser.urlencoded({ extended: true}));

var data;

function getCurrentTime(){
	var date = new Date();
	var hours = date.getHours() % 12 + 1;
	var minutes = date.getMinutes();
	var minString = minutes.toString();
	if (minutes < 10){
		minString = '0' + minString;
	}

	var ret = hours.toString() + ":" + minString;
	console.log(ret);
}

app.get('/',function(req,res){
	var time = getCurrentTime();	
	if (data === undefined){
		data = {temperature: 80, humidity: 20,pressure: 29};
	}
	res.render('home',{data: data});
});

app.post('/updateWeather',function(req,res){
	data = req.body;
	res.redirect("/");
});

/*********************************************************************
*
*		Uncomment the following block to run the code
*		on localhost:3000 for local debugging
*
**********************************************************************/
app.listen(3000,function(){
	console.log('Server initialized.')
});

/* app.listen(process.env.PORT, process.env.IP); */
