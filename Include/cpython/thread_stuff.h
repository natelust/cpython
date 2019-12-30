#include <stdatomic.h>
#include <pthread.h>

#ifndef Py_THREAD_STUFF_H
#define Py_THREAD_STUFF_H

# define NUMBER_THREADS_CXE 50

typedef struct thread_marker {
    unsigned short is_marker;
    uint32_t wait_count;
    pthread_mutex_t *locks[NUMBER_THREADS_CXE];    
} thread_marker;

typedef struct thread_barrier {
    thread_marker * thread_marker_pointer;
} thread_barrier;

#endif