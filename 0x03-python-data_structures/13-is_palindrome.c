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
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL, *midnode = NULL;
	int is_palindrome = 1;

	/* empty or single list is palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	/* if the list is odd the fast pointer is not null */
	if (fast != NULL)
	{
		midnode = slow;
		slow = slow->next; /* move to the second half */
	}
	/* terminate the first half and reverse the second half */
	prev_slow->next = NULL;
	reverse(&slow);

	is_palindrome = compare_lists(*head, slow);

	/* construct the original list back */
	reverse(&slow);
	if (midnode != NULL)
	{
		prev_slow->next = midnode;
		midnode->next = slow;
	} else
		prev_slow->next = slow;
	return (is_palindrome);
}

/** reverse - reverse a singly linked list
 * @head: pointer to pointer to head
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL, *current = *head;

	while (current != NULL)
	{
		*head = current->next;
		current->next = prev;
		prev = current;
		current = *head;
	}
	*head = prev;
}

/** compare_lists - check if two singly linked lists are equal
 * @head1: pointer to the first list
 * @head2: pointer to the second list
 *
 * Return: 1 if the linked lists are equal otherwise 0
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}
