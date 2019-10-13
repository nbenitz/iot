
var topic = 'clients/arduino/192.168.43.146/#';

var ledtopic = 'clients/arduino/led'	// Web PUBlishes to ledtopic + "/cmd"

var tempGauge;

var arduinoTemp = new Array();

var connected_flag = 0;

var mqtt;
var reconnectTimeOut = 2000;
var host = 'broker.mqttdashboard.com';
var port   = 8000;
var stopic = 'clients/arduino/#';

function onConnectionLost() {
	console.log("Conexion perdida");
	//document.getElementById("status").innerHTML = "Conexion perdida";
	//document.getElementById("messages").innerHTML = "Conexion perdida";
	connected_flag = 0;
	return false;
}

function onFailure() {
	console.log("Fallido");
	//document.getElementById("messages").innerHTML = "Conexion Fallida"
	setTimeout(MQTTconnect, reconnectTimeOut);
	return false;
}

function onMessageArrived(msg) {
	out_msg = "Msj: " + msg.payloadString + "\n";
	out_msg = out_msg + "Topic: " + msg.destinationName;
	console.log(out_msg);
	document.getElementById("temperatura").innerHTML = msg.payloadString + " &deg;C";
	
	return false;
}

function onConnected(recon, url) {
	console.log("en onConnected" + recon);
	return false;
}

function onConnect() {
	//document.getElementById("messages").innerHTML = "Conectado"
	connected_flag = 1;
	//document.getElementById("status").innerHTML = "Conectado"
	console.log("Conectado: " + connected_flag);
	sub_topics();
}

function MQTTconnect() {
/*	document.getElementById("status").innerHTML = "Conectando..";
	var s = document.forms["connform"]["server"].value;
	var p = document.forms["connform"]["port"].value;

	if (p != "") {
		port = parseInt(p);
		console.log("port " + port);
	}

	if (s != "") {
		host = s;
		console.log("host " + host);
	}*/
	console.log("Conectando a " + host + " " + port);
	mqtt = new Paho.MQTT.Client(host, port, "web_" + parseInt(Math.random() * 100, 10));
	
	var options = {
		timeout: 3,
		onSuccess: onConnect,
		onFailure: onFailure,
	}
	mqtt.onConnectionLost = onConnectionLost;
	mqtt.onMessageArrived = onMessageArrived;
	//mqtt.onConnected = onConnected;
	mqtt.connect(options);
	return false;
}

function sub_topics() {
	//document.getElementById("messages").innerHTML = "";
	if (connected_flag == 0) {
		out_msg = "<b>Not Connected so can't subscribe</b>";
		console.log(out_msg);
		//document.getElementById("messages").innerHTML = out_msg;
		return false;
	}
	//stopic = document.forms["subs"]["Stopic"].value;
	console.log("Subscribing to topic " + stopic);
	mqtt.subscribe(stopic);
	return false;
}

function send_message() {
	document.getElementById("messages").innerHTML = "";
	if (connected_flag == 0) {
		out_msg = "Not Connected so can't send massages";
		console.log(out_msg);
		document.getElementById("messages").innerHTML = out_msg;
		return false;
	}
	var msg = document.forms["smessage"]["message"].value;
	//var msg = document.forms["smessage"]["message"].value;
	console.log(msg);

	var topic = document.forms["smessage"]["Ptopic"].value;
	message = new Paho.MQTT.Message(msg);
	if (topic == "")
		message.destinationName = "test-topic";
	else
		message.destinationName = topic;
	mqtt.send(message);
	return false;
}

MQTTconnect();


