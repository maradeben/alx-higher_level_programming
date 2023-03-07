#include "lists.h"

/**
 * insert_node: insert node in sorted linked list
 * @head: pointer to the head node
 * number: number to insert
 * Return: address of new node, or null if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (prev == NULL || new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	/* insert to head if least */
	if (number < current->n || current == NULL)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (number > current->n && current->next != NULL)
	{
		prev = current;
		current = current->next;
	}


	/* case: number is greater than tail node */
	if (number > current->n)
	{
		current->next = new;
		new->next = NULL;
		return (new);
	}
	new->next = current;
	prev->next = new;

	return (new);
}

