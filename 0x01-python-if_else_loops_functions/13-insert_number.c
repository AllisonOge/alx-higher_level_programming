#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head pointer
 * @number: number to be inserted
 *
 * Return: pointer to the new node otherwise NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	/* create node */
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!current)
		*head = new; /* update the head */
	else
	{
		if (current->n > number)
		{
			new->next = current; /* insert at the beginning */
			*head = new; /* update the head */
		} else
		{
			while (current->next && current->next->n < number)
				current = current->next;
			/* insert the new node */
			new->next = current->next;
			current->next = new;
		}
	}
	return (new);
}
