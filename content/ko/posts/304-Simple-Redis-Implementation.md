---
title: "Simple Redis Implementation"
date: 2024-06-20T14:46:04+09:00
slug: "304-Simple-Redis-Implementation"
original_url: "https://memoryhub.tistory.com/304"
tistory_id: 304
draft: false
categories: ["데브 데이터베이스"]
tags: ["Redis"]
---

*Implementing a messaging system with Redis involves using its Pub/Sub feature, which allows for efficient and real-time message broadcasting and subscription.*

### The Big Picture

Imagine a messaging system like a public announcement system in a school. Redis’ Pub/Sub feature is the microphone and speakers setup, where someone speaks into the microphone (publishes a message) and anyone in the school can hear it if they are listening through the speakers (subscribed to the channel).

### Core Concepts

1. **Channels**: These are the "topics" to which messages are sent. Anyone interested in a particular topic can subscribe to the corresponding channel.
2. **Publishers**: Entities that send messages to a channel. They are like the person speaking into the microphone.
3. **Subscribers**: Entities that listen for messages on a channel. They are like the students listening through the speakers.

### Detailed Walkthrough

#### Setting Up a Simple Messaging System

1. **Start Redis Server**: Ensure you have Redis installed and running.
2. `redis-server`
3. **Publish/Subscribe Basics**: Use the `PUBLISH` and `SUBSCRIBE` commands to send and receive messages.
4. **Publish a Message**:
   - **Command**: `PUBLISH channel message`
   - **Example**: A user sends a message to the "chatroom" channel.

     ```
     redis-cli PUBLISH chatroom "Hello, World!"
     ```
5. **Subscribe to a Channel**:
   - **Command**: `SUBSCRIBE channel`
   - **Example**: A user subscribes to the "chatroom" channel to receive messages.

     ```
     redis-cli SUBSCRIBE chatroom
     ```

### Understanding Through an Example

Let's create a simple chat application where users can send messages to a channel and receive messages from it.

#### Step-by-Step Implementation

1. **Publisher Script**: A script for sending messages.
2. `import redis
   def publish_message(channel, message):
   r = redis.Redis(host='localhost', port=6379, db=0)
   r.publish(channel, message)
   print(f"Message '{message}' published to channel '{channel}'.")
   if __name__ == "__main__":
   channel = "chatroom"
   message = "Hello, this is a test message!"
   publish_message(channel, message)`
3. **Subscriber Script**: A script for receiving messages.
4. `import redis
   def message_handler(message):
   print(f"Received message: {message['data']}")
   def subscribe_channel(channel):
   r = redis.Redis(host='localhost', port=6379, db=0)
   p = r.pubsub()
   p.subscribe(**{channel: message_handler})
   print(f"Subscribed to channel '{channel}'. Waiting for messages...")
   p.run_in_thread(sleep_time=0.001)
   if __name__ == "__main__":
   channel = "chatroom"
   subscribe_channel(channel)`

### Conclusion and Summary

To implement a simple messaging system with Redis, you utilize the Pub/Sub mechanism, where you define channels for communication. Publishers send messages to these channels, and subscribers listen for messages from the channels. This setup is efficient for real-time messaging applications like chat systems or notifications.

### Test Your Understanding

1. What is the role of the `SUBSCRIBE` command in Redis?
2. How does the `PUBLISH` command work, and what happens when it is executed?
3. Can a single Redis client subscribe to multiple channels simultaneously? If so, how?

### Reference

For more information on Redis Pub/Sub, refer to the [official Redis documentation](https://redis.io/topics/pubsub).
