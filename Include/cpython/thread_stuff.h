#include <stdatomic.h>
#include <pthread.h>

#ifndef Py_THREAD_STUFF_H
#define Py_THREAD_STUFF_H

# define NUMBER_THREADS_CXE 9000

typedef struct thread_marker {
    int32_t wait_count;
    pthread_mutex_t *locks[NUMBER_THREADS_CXE];    
} thread_marker;

#endif