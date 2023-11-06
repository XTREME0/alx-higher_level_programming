#include "lists.h"
#include <stdio.h>
#include <string.h>
/**
 * is_palindrome: checks if list is palindrome duuh
 * @head: head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int l = 0, i = 0;
	listint_t *ptr;
	int lst[500];

	ptr = *head;
	while (ptr->next != NULL)
	{
		l++;
		lst[i] = ptr->n;
		i++;
		ptr = ptr->next;
	}
	lst[i] = ptr->n;
	l++;
	if (l == 0)
		return 1;
	for (i = 0; i < (l / 2); i++)
	{
		if (lst[i] != lst[l - i - 1])
			return 0;
	}
	return 1;
}
