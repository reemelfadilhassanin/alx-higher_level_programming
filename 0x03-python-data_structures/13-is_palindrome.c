#include "lists.h"
#include <stddef.h>

/**
 * aux_palind - function to know if palindrome
 * @left: head list
 * @end: end list
*/
int aux_palind(listint_t **left, listint_t *end)
{
	 if (end == NULL)
	 return (1);
	 if (aux_palind(left, end->next) && (*left)->n == end->n)
	 {
		*left = (*left)->next;
		return (1);
	 }
	 return (0);
}
    

/**
 * is_palindrome - checks list is a palindrome
 *
 * @head: the head address of list
 *
 * Return: 1 if it's a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	   return (1);
	return (aux_palind(head, *head));
}
