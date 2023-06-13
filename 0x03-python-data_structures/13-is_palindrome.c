#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: pointer to the head of listint_t
 *
 * Return: 1 if palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head; /* pointer to fill the stack */
	int stack[1024], i = 0; /* declare the stack */

	/* populate the stack with the singly linked list */
	while (slow != NULL)
	{
		stack[i++] = slow->n;
		slow = slow->next;
	}
	i--; /*adjust index to point to the top of the stack */

	/* iterate again over the list and check if palindrome */
	while (*head != NULL)
	{
		if ((*head)->n != stack[i--])
			return (0);
		/* increment node pointer*/
		*head = (*head)->next;
	}
	return (1);
}
