#include <stdatomic.h>
#include <pthread.h>

#ifndef Py_THREAD_STUFF_H
#define Py_THREAD_STUFF_H

# define NUMBER_THREADS_CXE 10000

typedef struct thread_marker {
    int64_t wait_count;
    pthread_mutex_t **locks;    
} thread_marker;

#endif