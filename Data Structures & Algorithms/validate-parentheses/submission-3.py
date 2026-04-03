class Solution:
    def isValid(self, s: str) -> bool:
    
        hashMap = {")":"(", "]":"[", "}":"{"}
        opening = "([{"
        stack = []
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    if hashMap[s[i]]!= stack[-1]:
                        return False
                    else:
                        stack.pop()
                
        return stack==[]


            # if s[i] in opening:
            #     open_stack.append(s[i])
            # if s[i] in closing:
            #     # fetch last openstack
            #     top_close = open_stack.pop()
            #     if 
            


            # for j in range(len(s)-1, -1, -1):
            #     if 