"""Notification channels for django-notifs."""

from json import dumps
import os
import logging
import pika

from notifications.channels import BaseNotificationChannel


class BroadCastWebSocketChannel(BaseNotificationChannel):
    """Fanout notification channel with RabbitMQ."""

    def _connect(self):
        """Connect to the RabbitMQ server."""
        # connection = pika.BlockingConnection(
        #     pika.ConnectionParameters(host='localhost')
        # )
        host = os.environ.get("RABBITMQ_HOST", "rabbitmq")
        port = int(os.environ.get("RABBITMQ_PORT", "5672"))
        user = os.environ.get("RABBITMQ_DEFAULT_USER", "guest")
        password = os.environ.get("RABBITMQ_DEFAULT_PASS", "guest")

        credentials = pika.PlainCredentials(user, password)
        params = pika.ConnectionParameters(
            host=host,
            port=port,
            credentials=credentials,
            heartbeat=600,
            blocked_connection_timeout=300,
        )
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        return connection, channel

    def construct_message(self):
        """Construct the message to be sent."""
        extra_data = self.notification_kwargs['extra_data']

        return dumps(extra_data['message'])

    def notify(self, message):
        """put the message of the RabbitMQ queue."""
        connection, channel = self._connect()

        uri = self.notification_kwargs['extra_data']['uri']

        channel.exchange_declare(exchange=uri, exchange_type='fanout')
        channel.basic_publish(exchange=uri, routing_key='', body=message)

        connection.close()
