class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapping = {}
        curr = head

        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            mapping[curr].next = mapping.get(curr.next)
            mapping[curr].random = mapping.get(curr.random)
            curr = curr.next

        return mapping[head]