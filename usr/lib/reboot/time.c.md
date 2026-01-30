```c
#include <time.h>
#include <stdio.h>

int main(int argc, char **argv) {
    time_t *t;
    printf("time since the epoch: %ld\n", time(t));
}
```