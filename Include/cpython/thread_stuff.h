#include <stdatomic.h>
#include <pthread.h>

#ifndef Py_THREAD_STUFF_H
#define Py_THREAD_STUFF_H

# define NUMBER_THREADS_CXE 10000

typedef struct thread_marker {
    int64_t wait_count;
    PyThreadState *locks[NUMBER_THREADS_CXE];
} thread_marker;

typedef struct multi_thread {
    _Bool upgrade
} multi_thread;

#endif