

var connected_flag = 0;

var mqtt;
var reconnectTimeOut = 2000;
//var host = 'broker.hivemq.com';
//var host = 'test.mosquitto.org';
//var port   = 8080;
var host = 'broker.mqtt-dashboard.com'
var port = 8000;
var user;
var sensor_topic = 'myiot87/sensor/#';
var online_topic = 'myiot87/online/#';
var actuator_topic = 'myiot87/control/';
var feedback_topic = 'myiot87/feedback/#';

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
		if ($("#sensor-puerta-" + id_sensor)) {
			var state = msg.payloadString;
			if (state == "0") {
				if ($("#border-" + id_sensor).hasClass('border-left-danger')) {
					$('#border-' + id_sensor).removeClass('border-left-danger').addClass('border-left-success');
					$('#txt-' + id_sensor).removeClass('text-danger').addClass('text-success');
					$('#icon-' + id_sensor).removeClass('text-danger').addClass('text-success');
				}
			}
			if (state == "1") {
				if ($("#border-" + id_sensor).hasClass('border-left-success')) {
					$('#border-' + id_sensor).removeClass('border-left-success').addClass('border-left-danger');
					$('#txt-' + id_sensor).removeClass('text-success').addClass('text-danger');
					$('#icon-' + id_sensor).removeClass('text-success').addClass('text-danger');
				}
			}
		}
		else if ($("#sensor-" + id_sensor)) {
			$("#sensor-" + id_sensor).text(msg.payloadString);
			if ($("#progress-" + id_sensor)) {
				var min = $("#progress-" + id_sensor).attr('aria-valuemin');
				var max = $("#progress-" + id_sensor).attr('aria-valuemax');
				var now = msg.payloadString;
				var siz = (now - min) * 100 / (max - min);
				$("#progress-" + id_sensor).attr('style', 'width:' + siz + '%');
				//$("#progress-" + id_sensor).attr('style', 'width:' + msg.payloadString + '%');
			}
		}
	}
	if (sub_topic == 'feedback') {
		var id_actuador = topic_parts[2];
		if ($("#actuador-" + id_actuador)) {
			if (msg.payloadString == '1') {
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

	mqtt = new Paho.MQTT.Client(host, port, "web_" + parseInt(Math.random() * 100, 10),);

	var options = {
		timeout: 3,
		onSuccess: onConnect,
		onFailure: onFailure,
		cleanSession: false,
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
	console.log("Subscribing to topic " + online_topic);
	mqtt.subscribe(sensor_topic);
	mqtt.subscribe(feedback_topic);
	mqtt.subscribe(online_topic);
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

	var topic = actuator_topic + id;
	message = new Paho.MQTT.Message(msg);
	message.destinationName = topic;
	console.log("-> " + topic + " | " + msg);
	mqtt.send(message);
	return false;
}

function hideAlert() {
	$("#messages").fadeTo(2000, 500).slideUp(500, function () {
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


