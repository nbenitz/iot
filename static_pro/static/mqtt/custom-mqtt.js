
//var topic = 'clients/arduino/192.168.43.146/#';

//var ledtopic = 'clients/arduino/led'	// Web PUBlishes to ledtopic + "/cmd"

var tempGauge;

var arduinoTemp = new Array();

var connected_flag = 0;

var mqtt;
var reconnectTimeOut = 2000;
//var host = 'broker.hivemq.com';
var host = 'test.mosquitto.org';
var port   = 8080;
var sensor_topic = 'yonestor87@gmail.com/sensor/#';
var feedback_topic = 'yonestor87@gmail.com/feedback/#';
var lwt_topic = 'yonestor87@gmail.com/lwt/#';
var pub_topic = 'yonestor87@gmail.com/control/';

function onConnectionLost() {
	console.log("Conexion perdida");
	$("#messages").text("Conexion perdida");	
	dangerAlert();
	$("#messages").show();	
	
	connected_flag = 0;
	MQTTconnect();
	return false;
}

function onFailure() {
	console.log("Fallido");
	
	//$("#messages").text("Conexion Fallida");	
	dangerAlert();
	
	setTimeout(MQTTconnect, reconnectTimeOut);
	return false;
}

function onMessageArrived(msg) {
	out_msg = "<- " + msg.destinationName + " | " + msg.payloadString;
	console.log(out_msg);
	
	var topic_parts = msg.destinationName.split('/');
	if (topic_parts.length < 3) {
		return;
	}
	
	var sub_topic = topic_parts[1];
	
	if (sub_topic == 'sensor') {
		var id_sensor = topic_parts[2];
		if ($("#sensor-" + id_sensor )) {
			$("#sensor-" + id_sensor).text(msg.payloadString);
			if ( $("#progress-" + id_sensor )) {
				$("#progress-" + id_sensor).attr('style', 'width:' + msg.payloadString + '%');
			}
		}
	}
	if (sub_topic == 'feedback') {
		var id_actuador = topic_parts[2];
		if ( $("#actuador-" + id_actuador )) {
			if (msg.payloadString == '1'){
				$("#actuador-" + id_actuador).text("On");
				$('#act-crd-' + id_actuador).removeClass('border-left-danger').addClass('border-left-success');
				$('#act-txt-' + id_actuador).removeClass('text-danger').addClass('text-success');
				$('#act-btn-' + id_actuador).removeClass('btn-danger').addClass('btn-success');
			} else {
				if (msg.payloadString == '0') {
					$("#actuador-" + id_actuador).text("Off");
					$('#act-crd-' + id_actuador).removeClass('border-left-success').addClass('border-left-danger');
					$('#act-txt-' + id_actuador).removeClass('text-success').addClass('text-danger');
					$('#act-btn-' + id_actuador).removeClass('btn-success').addClass('btn-danger');
				}
			}
		}		
	}	
	
	return false;
}

function onConnected(recon, url) {
	console.log("en onConnected" + recon);
	return false;
}

function onConnect() {
	$("#messages").text("Conectado");
	successAlert();
	hideAlert();
	
	connected_flag = 1;
	console.log("Conectado: " + connected_flag);
	sub_topics();
}

function MQTTconnect() {
	console.log("Conectando a " + host + " " + port);
	
	$("#messages").text("Conectando con Servidor MQTT..");
	primaryAlert();
		
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
	console.log("Subscribing to topic " + sensor_topic);
	console.log("Subscribing to topic " + feedback_topic);
	console.log("Subscribing to topic " + lwt_topic);
	mqtt.subscribe(sensor_topic);
	mqtt.subscribe(feedback_topic);
	mqtt.subscribe(lwt_topic);
	return false;
}

function enviar_msj(id) {
	if (connected_flag == 0) {
		out_msg = "No Conectado. No es posible enviar mensajes";
		console.log(out_msg);
		$("#messages").text(out_msg);	
		dangerAlert();		
		return false;
	}
	var msg = "5";
	if ($("#actuador-" + id).text() == "On")
		msg = "0";
 	else 
		msg = "1";
		
	var topic = pub_topic + id;
	message = new Paho.MQTT.Message(msg);
	message.destinationName = topic;
	console.log("-> " + topic + " | " + msg);
	mqtt.send(message);
	return false;
}

function hideAlert() {
	$("#messages").fadeTo(2000, 500).slideUp(500, function() {
		$("#messages").slideUp(500);
	});
}

function dangerAlert() {
	if ($("#messages").hasClass('alert-primary')) {
		$('#messages').removeClass('alert-primary').addClass('alert-danger');	
	}
	if ($("#messages").hasClass('alert-success')) {
		$('#messages').removeClass('alert-success').addClass('alert-danger');
	}
}

function successAlert() {
	if ($("#messages").hasClass('alert-primary')) {
		$('#messages').removeClass('alert-primary').addClass('alert-success');	
	}
	if ($("#messages").hasClass('alert-danger')) {
		$('#messages').removeClass('alert-danger').addClass('alert-success');
	}
}

function primaryAlert() {
	if ($("#messages").hasClass('alert-danger')) {
		$('#messages').removeClass('alert-danger').addClass('alert-primary');	
	}
	if ($("#messages").hasClass('alert-success')) {
		$('#messages').removeClass('alert-success').addClass('alert-primary');
	}
}


