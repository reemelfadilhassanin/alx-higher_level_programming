#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks list is a palindrome
 *
 * @head: the head address of list
 *
 * Return: 1 if it's a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int val[2048];
    int i = 0;
    int j = 0;

    if (*head)
    {
       
        while (current)
        {
            val[i] = current->n;
            current = current->next;
            i++;
        }
        while (j < i / 2)
        {
            if (val[j] == val[i - j - 1])
                j++;
            else
                return (0);
        }
    }

    return (1);
