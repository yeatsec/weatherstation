// Weather update receiving server, stores information in shared file, launches display script
// Connnects to SUB socket tcp://localhost:5556

#include <unistd.h>
#include <stdio.h>
#include "zhelpers.h"

const char * PYTHON_PATH = "";
const char * SCRIPT_PATH = "";
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

		// call exec for bookkeeping script
		pid_t parent = getpid();
		pid_t pid = fork();

		if (pid == -1)
		{
			// fork failed
		}
		else if (pid > 0)
		{
			int status;
			waitpid(pid, &status, 0);
		}
		else
		{
			// child
			char * argv[5];
			argus[0] = PYTHON_PATH;
			argus[1] = SCRIPT_PATH;
			int retvar = sprintf(argus[2], "%ld", temp);
			if (retvar < 0)
			{
				printf("sprintf error\n");
			}
			retvar = sprintf(argus[3], "%ld", press);
			if (retvar < 0)
			{
				printf("sprintf error\n");
			}
			retvar = sprintf(argus[4], "%ld", hum);
			if (retvar < 0)
			{
				printf("sprintf error\n");
			}
			execve(argus[0], argus);
			printf("big bad error\n");
		}
	}
}