class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def build_tree_from_list(vals):
    if not vals:
        return None
    
    # Create the root node
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    
    while i < len(vals):
        current = queue.pop(0)
        
        # Assign left child if not None
        if vals[i] is not None:
            current.left = TreeNode(vals[i])
            queue.append(current.left)
        i += 1
        
        if i >= len(vals):
            break
        
        # Assign right child if not None
        if vals[i] is not None:
            current.right = TreeNode(vals[i])
            queue.append(current.right)
        i += 1
    
    return root


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []

        while queue != []: # while the queue is empty
            for root in queue: #for each value that is currently in the queue 
                level.append(root.val) #we want to append the values of the root to the level level[3,2]
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level) 
            level = []
            queue = next_queue
            next_queue = []

        return result




s = Solution()
print(s.levelOrder([3,9,20,None,None,15,7]))