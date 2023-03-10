#include "lists.h"

/**
 * is_palindrome - check if a lniked list is a palindrome
 * @head: pointer to head node
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *right = *head, *left = malloc(sizeof(listint_t));
	int n1, n2, i;

	n2 = list_len(*head);
	/* empty list is considered palindrome */
	if (head == NULL || n2 ==1)
		return (1);
	
	for (n1 = 0; n1 < n2; n1++, n2--)
	{
		/* reset left to head on starting each loop */
		left = *head;
		for (i = 0; i < n2; i++)
			left = left->next;
		if (right->n != left->n)
			return (0);
		right = right->next;
	}
	return (1);
}

/**
 * list_len - length of singly linked list
 * @h: pointer to head of list
 * Return: number of nodes in the list
 */
int list_len(listint_t *h)
{
	int count = 0;
	while (h != NULL)
	{
		count += 1;
		h = h->next;
	}
	return (count);
}
