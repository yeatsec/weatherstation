var express = require('express');
var app = express();
var logger = require('morgan');
var bodyParser = require('body-parser');
//var mongoose = require('mongoose')

app.use(express.static('public'));
app.set('view engine','ejs');
app.use(logger('dev'))
app.use(bodyParser.urlencoded({ extended: true}));

/*
mongoose.connect("mongodb://localhost/testapp");
var weatherSchema = new mongoose.Schema( {
	temperature: Number,
	humidity: Number
});
*/

//var WeatherData = mongoose.model("Weather",weatherSchema);

var data;

app.get('/',function(req,res){
	if (data === undefined){
		data = {temperature: 80, humidity: 20,pressure: 29};
	}
	res.render('home',{data: data});
});

app.post('/updateWeather',function(req,res){
	data = req.body;
	/*WeatherData.create({
		temperature: data.temperature,
		humidity: data.humidity
	},function(err){
		res.redirect("/home");
	});
	*/
	res.redirect("/");
});

/*
app.listen(3000,function(){
	console.log('Server initialized.')
});*/


app.listen(process.env.PORT, process.env.IP);
