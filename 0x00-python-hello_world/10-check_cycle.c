#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the listint_t list
 *
 * Return: 0 if there are no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	/* check if loop exist in the linked list */
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			/* loop detected */
			return (1);
	}
	return (0); /* no loop detected */
}
