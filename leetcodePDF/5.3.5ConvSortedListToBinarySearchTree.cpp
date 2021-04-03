
/* 把单链表转换为BST
# 	前面已经将排序数组转为BST 排序数组具有随机访问的特性,但是单链表不具有随机访问的特性

# https://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/

/* The main function that constructs  
balanced BST and returns root of it.  
head_ref --> Pointer to pointer to  
head node of linked list n --> No. 
of nodes in Linked List */
TNode* sortedListToBSTRecur(LNode **head_ref, int n)  
{  
    /* Base Case */
    if (n <= 0)  
        return NULL;  
  
    /* Recursively construct the left subtree */
    TNode *left = sortedListToBSTRecur(head_ref, n/2);  
  
    /* Allocate memory for root, and  
    link the above constructed left  
    subtree with root */
    TNode *root = newNode((*head_ref)->data);  
    root->left = left;  
  
    /* Change head pointer of Linked List 
    for parent recursive calls */
    *head_ref = (*head_ref)->next;  
  
    /* Recursively construct the right  
        subtree and link it with root  
        The number of nodes in right subtree 
        is total nodes - nodes in  
        left subtree - 1 (for root) which is n-n/2-1*/
    root->right = sortedListToBSTRecur(head_ref, n - n / 2 - 1);  
  
    return root;  
}  