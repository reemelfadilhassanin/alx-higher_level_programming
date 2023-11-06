#include "lists.h"
#include <stddef.h>

/**
 * aux_palind - function that check if a list is a palindrome recursively
 * @left: address to the left end of the current section
 * @end: address to the right end of the current section
 *
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int aux_palind(listint_t **left, listint_t *end)
{
	if (end == NULL)
		return (1);
	int is_palindrome = aux_palind(left, end->next);

	if (is_palindrome && (*left)->n == end->n)
	{
		*left = (*left)->next; 
		return (1); 
	}

	return (0); 
}

/**
 * is_palindrome - checks if a list is a palindrome
 *
 * @head: address to the head of the list
 *
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	return aux_palind(head, *head);
}
