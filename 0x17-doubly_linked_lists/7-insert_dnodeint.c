#include "lists.h"

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
    if (h == NULL)
        return NULL;

    if (idx == 0)
        return add_dnodeint(h, n);

    dlistint_t *new_node = malloc(sizeof(dlistint_t));
    if (new_node == NULL)
        return NULL;

    new_node->n = n;
    dlistint_t *current = *h;
    unsigned int i = 0;

    while (current != NULL)
    {
        if (i == idx - 1)
        {
            new_node->prev = current;
            new_node->next = current->next;

            if (current->next != NULL)
                current->next->prev = new_node;

            current->next = new_node;
            return new_node;
        }

        current = current->next;
        i++;
    }

    free(new_node);
    return NULL;
}

