#include "array_operations.hh"

int greatest_v1(int *itemptr, int size)
{
    int* arrayptr = itemptr;
    int biggest_nro = *itemptr;
    while (arrayptr < itemptr + size)
    {
        if (*arrayptr > biggest_nro)
            biggest_nro = *arrayptr;
        ++arrayptr;
    }
    return biggest_nro;
}

int greatest_v2(int *itemptr, int *endptr)
{
    int* arrayptr = itemptr;
    int biggest_nro = *itemptr;
    while (arrayptr < endptr)
    {
        if (*arrayptr > biggest_nro)
            biggest_nro = *arrayptr;
        ++arrayptr;
    }
    return biggest_nro;
}

void copy(int *itemptr, int *endptr, int *targetptr)
{
    while (itemptr < endptr)
    {
        *targetptr = *itemptr;
        ++ itemptr;
        ++ targetptr;
    }
}

void reverse(int *leftptr, int *rightptr)
{
    rightptr -= 1;
    int leftnum = 0;
    while (leftptr < rightptr)
    {
        leftnum = *leftptr;
        *leftptr = *rightptr;
        *rightptr = leftnum;
        ++leftptr;
        --rightptr;
    }
}
