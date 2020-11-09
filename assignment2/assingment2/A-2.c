#include <stdio.h>
#include "stack.h"
/* assume that stack doesnt get full */
int main() {
    stack s;
    int i;
    init(&s);
    for(i = 0; i < 8; i++)
        if(i % 3 == 0) 
            push(&s, i + 1);
        if(i % 5 == 0) 
            push(&s, i - 1);
    while(!isempty(&s))
        printf("%d\n", pop(&s));
    return 0;
}