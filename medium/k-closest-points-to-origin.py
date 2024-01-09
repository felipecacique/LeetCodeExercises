# https://leetcode.com/problems/k-closest-points-to-origin/


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Solution1: calculate all distances for each point, and sort the array, and return the k first items. Time 0(nlog(n)) fpr sorting the array.Istead of sorting, at each new point, we alredy process it comparing it to the closest_list (closest point fpund so far).

        # Solution2: as we calculate the distances, we create a binary search tree with the points, where the value is equal to the distance. Then we travel the tree and get the smallest values. time O(n*log(n)). The insertion is log(n) andwe need to insert n points. We wont do the sqrt operation. Actually we could have a (n*log(k)) since we do not need to create the entire tree, just a tree of size k, holding the smallest elements. Wen adding a new one (if it is smaller that the greattest), we have to remove the greattest, kepping its size constant.

        # Solution3: we calculate all distances. Then we create and array of size k, and we will add the k first points in sorted way O(k*log(k)). Then, for each new pointt, we checl if it would go inside the array (if the point distance is smaller than the max distance within the array) we add this new point to the array in sort order, and remode the last element. At the end of this process we will have and sorted array of size k with the minimum distances. Time(n*log(k))) where log(k) is the insertion in the array of size k, and we have to do it for all n elements. There is just one problem, if we work with list, addin a new element to the list could take O(k), and that is not good ... we could use a binary search tree instead since the complexity for insertion is O(log(k)). Actually this is the same solution as Solution2.

        def Solution2(points, k):  # it is not working fine ...
            class NodeTree:
                def __init__(self, val, point):
                    self.val = val
                    self.point = point
                    self.left = None
                    self.right = None

            class BinarySearchTree:
                def __init__(self, size=None):
                    self.size = size
                    self.node = None
                    self.largestDistance = float("inf")
                    self.length = 0

                def insert(self, new_node):
                    def insert(node, new_node):  # recursive
                        if node is None:
                            self.length += 1
                            return new_node

                        if new_node.val < node.val:
                            node.left = insert(node.left, new_node)
                        else:
                            node.right = insert(node.right, new_node)

                        return node

                    if self.node is None:
                        self.node = new_node
                        self.largestDistance = new_node.val
                        self.length = 1
                    else:
                        insert(self.node, new_node)
                        self.largestDistance = max(self.largestDistance, new_node.val)

                def deleteNodeLargest(self):
                    deleted = [False]

                    def deleteNodeLargest(node):
                        # The largest element will be always the last leaf on the very right.
                        if node is None:
                            self.length = max(0, self.length - 1)
                            return None

                        self.largestDistance = max(self.largestDistance, node.val)
                        node.right = deleteNodeLargest(node.right)
                        if node.right is None and deleted[0] == False:
                            node = None
                            deleted[0] = True

                        return node

                    if self.length <= 1:
                        self.node = None
                        self.length = 0
                        self.largestDistance = float("inf")

                    else:
                        self.largestDistance = self.node.val
                        deleteNodeLargest(self.node)

                def treeToArray(self):
                    # return an array with all points
                    arr = []

                    def treeToArray(node):
                        if node is None:
                            return None

                        treeToArray(node.left)
                        treeToArray(node.right)

                        if node:
                            arr.append(node.point)

                        return node

                    treeToArray(self.node)

                    return arr

            # points = [[3, 3], [5, -1], [-2, 4]]
            # k = 2

            bst = BinarySearchTree()
            # distance = points[0][0]*points[0][0] + points[0][1]*points[0][1]
            # bst.node = NodeTree(distance, points[0])

            for point in points:  # O(n)
                distance = (
                    point[0] * point[0] + point[1] * point[1]
                )  # we will remove the sqrt, since it is not necessary and is time expensive
                # print(distance, bst.largestDistance)
                if distance < bst.largestDistance or bst.length < k:  # O(log(k))
                    if bst.length >= k:
                        bst.deleteNodeLargest()  # this ensure that the tree size is smaller or equal than k
                    node = NodeTree(distance, point)
                    bst.insert(
                        node
                    )  # this method will add a new point node to the binary search tree, in order

            # print(bst.treeToArray())  # return the points in an array

            return bst.treeToArray()  # return the points in an array

        # Solution 4: using a min heap. The creatinon of the heap is the miraculous O(n). We need to pop k elements O(k). So the complexity is O(klog(n)). I have got the solution from the source: https://www.youtube.com/watch?v=rI2EBUEMfTk&ab_channel=NeetCode

        def Solution4(points, k):
            import heapq

            minHeap = []
            for x, y in points:
                dist = (x**2) + (y**2)
                minHeap.append([dist, x, y])

            heapq.heapify(minHeap)
            res = []
            while k > 0:
                dist, x, y = heapq.heappop(minHeap)
                res.append([x, y])
                k -= 1

            return res

        return Solution4(points, k)
