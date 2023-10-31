#include "lists.h"
#include "stdlib.h"

/**
 * insert_node - Inserts  into a sorted list.
 * @head: A head pointer of the linked list.
 * @number: The number to insert.
 *
 * Return: A pointer to the new node or NULL otherwise.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;

	if (!head)
		return NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (number < current->n)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next)
		{
			if (number > current->next->n)
				current = current->next;
			else
				break;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
