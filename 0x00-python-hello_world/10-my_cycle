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
	int length = 1, i = 0;
	listint_t **ptrs[1000];

	ptrs[0] = &list;
	while (list != NULL)
	{
		list = list->next;
		ptrs[length] = &list;
		length++;
		for (i = 0; i < length; i++)
		{
			if (ptrs[length] == &list)
				return (1);
		}
	}
	return (0);
}
