# class Solution:
#     def climbStairs(self, n: int) -> int:
#         l = [[0]]
#         for i in range(n):
#             for o in l:
#                 if sum(o) == i:
#                     c = o.copy()
#                     o.append(2)
#                     c.append(1)
#                     l.append(c)
#         b = []
#         for i in l:
#             if not sum(i) == n:
#                 b.append(i)
#         for i in b:
#             l.remove(i)

#         print(l)
#         return(len(set(tuple(x) for x in l)))
                

# obj = Solution()
# print(obj.climbStairs(35))

# class Solution:
#     def climbStairs(self, n: int) -> int:
#        if n<3:
#            return n
#        else:
#            return ((n-2) + (n-1))

# obj = Solution()
# print(obj.climbStairs(5))

print("ich habe aufgegeben")