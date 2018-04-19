// Weather update receiving server, stores information in shared file, launches display script
// Connnects to SUB socket tcp://localhost:5556

#include "zhelpers.h"

const char MAX_MESS_SIZE = 255;

int main (int argc, char *argv[])
{
	// create socket
	void *context = zmq_ctx_new();
	void * subscriber = zmq_socket(context, ZMQ_SUB);
	int rc = zmq_connect(subscriber, "tcp://localhost:5556"); // not sure if TCP is the best protocol for this setup
	assert (rc == 0);

	rc = zmq_setsockopt(subscriber, ZMQ_SUBSCRIBE, NULL, MAX_MESS_SIZE);
	assert(rc==0);

	while(1)
	{
		char * message = s_recv(subscriber); // will wait here for a message, could be non-null terminated
		double temp, press, hum;
		sscanf (message, "%lf %lf %lf", &temp, &press, &hum);
		free(message);
	}
}