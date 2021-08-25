# Kafka
Apache Kafka is a framework implementation of a software bus using stream-processing. It is an open-source software platform developed by the Apache Software Foundation written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.
## Messaging System
A messaging system is a simple exchange of messages between two or more persons, devices, etc. A publish-subscribe messaging system allows a sender to send/write the message and a receiver to read that message. In Apache Kafka, a sender is known as a producer who publishes messages, and a receiver is known as a consumer who consumes that message by subscribing it.
## Streaming Process
A streaming process is the processing of data in parallelly connected systems. This process allows different applications to limit the parallel execution of the data, where one record executes without waiting for the output of the previous record. Therefore, a distributed streaming platform enables the user to simplify the task of the streaming process and parallel execution. Therefore, a streaming platform in Kafka has the following key capabilities:
- As soon as the streams of records occur, it processes it.
- It works similar to an enterprise messaging system where it publishes and subscribes streams of records.
- It stores the streams of records in a fault-tolerant durable way.

1. **Producer API:** This API allows/permits an application to publish streams of records to one or more topics. 
2. **Consumer API:** This API allows an application to subscribe one or more topics and process the stream of records produced to them.
3. **Streams API:** This API allows an application to effectively transform the input streams to the output streams. It permits an application to act as a stream processor which consumes an input stream from one or more topics, and produce an output stream to one or more output topics.
4. **Connector API:** This API executes the reusable producer and consumer APIs with the existing data systems or applications.

## Why Apache Kafka
1. Apache Kafka is capable of handling millions of data or messages per second.
2. Apache Kafka works as a mediator between the source system and the target system. Thus, the source system (producer) data is sent to the Apache Kafka, where it decouples the data, and the target system (consumer) consumes the data from Kafka.
3. Apache Kafka is having extremely high performance, i.e., it has really low latency value less than 10ms which proves it as a well-versed software.
4. Apache Kafka has a resilient architecture which has resolved unusual complications in data sharing.
5. Organizations such as NETFLIX, UBER, Walmart, etc. and over thousands of such firms make use of Apache Kafka.
6. Apache Kafka is able to maintain the fault-tolerance. Fault-tolerance means that sometimes a consumer successfully consumes the message that was delivered by the producer. But, the consumer fails to process the message back due to backend database failure, or due to presence of a bug in the consumer code. In such a situation, the consumer is unable to consume the message again. Consequently, Apache Kafka has resolved the problem by reprocessing the data.

## Installation of Apache Kafka
Apache Kafka is supportable on Windows, macOS, as well as on Linux environment. Each operating system has its own steps/process to install Apache Kafka.

- **Step 1:** To install Apache Kafka, the java8 JDK kit should be installed on the system. If it is already installed, but with other versions, the user needs to reinstall Java. Because the current Kafka version supports java8 only. Use 'java -version' to check the version on the Windows command prompt. In case to install java8, use the following link: https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
- **Step2:** Now, download Apache Kafka on the system, Use the link: https://kafka.apache.org/downloads
- **Step3:** Click on the link and download any binary from Binary downloads.
- **Step4:** Go to the respective downloads location and extract the downloaded file using 7-zip. After extracting the file, it will be converted into a folder.
- **Step5:** Copy the Kafka folder to the root directory.
- **Step6:** Check the java version whether it is successfully installed or not.
- **Step7:** Try running some kafka commands.

## Kafka Producers
A producer is the one which publishes or writes data to the topics within different partitions. Producers automatically know that, what data should be written to which partition and broker. The user does not require to specify the broker and the partition.

A producer uses following strategie//s to write data to the cluster:
- Message Keys
- Acknowledgment

## Message Keys
Apache Kafka enables the concept of the key to send the messages in a specific order. The key enables the producer with two choices, i.e., either to send data to each partition (automatically) or send data to a specific partition only. Sending data to some specific partitions is possible with the message keys. If the producers apply key over the data, that data will always be sent to the same partition always. But, if the producer does not apply the key while writing the data, it will be sent in a round-robin manner. This process is called load balancing. In Kafka, load balancing is done when the producer writes data to the Kafka topic without specifying any key, Kafka distributes little-little bit data to each partition.

Therefore, a message key can be a string, number, or anything as we wish.

There are two ways to know that the data is sent with or without a key:
1. If the value of key=NULL, it means that the data is sent without a key. Thus, it will be distributed in a round-robin manner (i.e., distributed to each partition).
2. If the value of the key!=NULL, it means the key is attached with the data, and thus all messages will always be delivered to the same partition.

## Acknowledgment
In order to write data to the Kafka cluster, the producer has another choice of acknowledgment. It means the producer can get a confirmation of its data writes by receiving the following acknowledgments:

1. **acks=0:** This means that the producer sends the data to the broker but does not wait for the acknowledgement. This leads to possible data loss because without confirming that the data is successfully sent to the broker or may be the broker is down, it sends another one.
2. **acks=1:** This means that the producer will wait for the leader's acknowledgement. The leader asks the broker whether it successfully received the data, and then returns feedback to the producer. In such case, there is limited data loss only.
3. **acks=all:** Here, the acknowledgment is done by both the leader and its followers. When they successfully acknowledge the data, it means the data is successfully received. In this case, there is no data loss.

## Consumer and Consumer Groups
- A **consumer** is the one that consumes or reads data from the Kafka cluster via a topic. A consumer also knows that from which broker, it should read the data. The consumer reads the data within each partition in an orderly manner. It means that the consumer is not supposed to read data from offset 1 before reading from offset 0. Also, a consumer can easily read data from multiple brokers at the same time.
- A **consumer group** is a group of multiple consumers which visions to an application basically. Each consumer present in a group reads data directly from the exclusive partitions. In case, the number of consumers are more than the number of partitions, some of the consumers will be in an inactive state. Somehow, if we lose any active consumer within the group then the inactive one can takeover and will come in an active state to read the data.

## Consumer Offset
Apache Kafka provides a convenient feature to store an offset value for a consumer group. It stores an offset value to know at which partition, the consumer group is reading the data. As soon as a consumer in a group reads data, Kafka automatically commits the offsets, or it can be programmed. These offsets are committed live in a topic known as **__consumer_offsets.** This feature was implemented in the case of a machine failure where a consumer fails to read the data. So, the consumer will be able to continue reading from where it left off due to the commitment of the offset.

## Delivery Semantics
The choice of commitment depends on the consumer, i.e., when the consumer wishes to commit the offsets. Committing an offset is like a bookmark which a reader uses while reading a book or a novel.

In Kafka, there are following three delivery semantics used:

- **At most once:** Here, the offsets are committed as soon as the consumer receives the message.. But in case of incorrect processing, the message will be lost, and the consumer will not be able to read further. Therefore, this semantic is the least preferred one.
- **At least once:** Here, the offsets are committed after the message has been processed. If the processing goes wrong, then the message will be read again by the consumer. Therefore, this is usually preferred to use. Because a consumer can read the message twice, it results in duplicate processing of the messages. Thus, it needs a system to be an idempotent system.
- **Exactly once:** Here, the offsets can be achieved for Kafka to Kafka workflow only using the Kafka Streams API. For achieving offset for Kafka to the external system, we need to use an idempotent consumer.
