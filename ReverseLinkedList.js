// This took so long. I kept getting caught up thinking I would need a temporary
// variable to store current before I changed the .next attribute, which
// sent me down a rabbit hole trying to account for the way Javascript treats
// objects. Then I realized that wasn't necessary, since I would rewrite curr.next
// in the next iteration
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const reverseList = function(head) {
    if (!head) { return head}
    let prev = null;
    let curr = head; // curr.next = head.next
    while (curr != null){
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    }
    return prev;
}

// Recursive
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}yy
 */
var reverseList = function(head) {
    if (!head || !head.next) { return head }
    nextNode = head.next
    newHead = reverseList(nextNode)
    console.log(nextNode)
    nextNode.next = head
    nextNode = nextNode.next
    head.next = null
    return newHead
}
// It's clear I still need to work harder to understand recursion, as it's still
// very difficult for me to wrap my mind around how this solution works. I understand
// that we are using the call stack to store information about previously visited
// nodes, but I can't keep track of the winding and unwinding.
