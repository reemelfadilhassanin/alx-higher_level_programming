#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is cycle - 1.
 *         otherwise - 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list , *sec = list;

	while (sec && sec ->next)
	{
        first = first ->next;
        sec = sec->next->next;
    
		if (first == sec)
			return (1);

	
	}

	return (0);
}
