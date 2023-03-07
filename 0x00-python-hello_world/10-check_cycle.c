#include "lists.h"

/**
 * check_cycle - checks if a linked-list contains a cycle
 * @list: pointer to the head of list
 * Description: loop through nodes in the list, store addresses in list
 * check list on each loop to see if address is already present
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list, *ptr2 = list;

	while (ptr1 && ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
