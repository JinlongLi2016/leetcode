
# My Solution: Using A Stack 
class Solution:
    def trap(self, height: List[int]) -> int:
        Stack = []
        s = 0
        height = [0] + height + [0]
        for idx, h in enumerate(height):
            while len(Stack) > 0 and height[Stack[-1]] < h:
                if len(Stack) > 1:
                    s += (min(height[Stack[-2]], h) - height[Stack[-1]]) * (idx - Stack[-2] - 1)
                Stack.pop()
            if len(Stack) == 0 or height[Stack[-1]] > h:
                Stack.append(idx)
            else:
                Stack.pop()
                Stack.append(idx)

        return s
        
# My 2nd Solution 
def trap(height):
    hidx = 0
    for idx, h in enumerate(height):
        if h > height[hidx]:
            hidx = idx
    s = 0
    lh = 0
    for idx in range(1, hidx):
        if height[idx] >= height[lh]:
            lh = idx 
        else:
            s += min(height[lh], height[hidx]) - height[idx]
    
    rh = len(height) - 1
    for idx in range(rh, hidx, -1):
        if height[idx] >= height[rh]:
            rh = idx 
        else:
            s += min(height[rh], height[hidx]) - height[idx]
    return s 
    

# Leetcode Solution
# https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c%2B%2B-code%3A-O(n)-time-O(1)-space
class Solution {
    public:
        int trap(int A[], int n) {
            int left=0; int right=n-1;
            int res=0;
            int maxleft=0, maxright=0;
            while(left<=right){
                if(A[left]<=A[right]){
                    if(A[left]>=maxleft) maxleft=A[left];
                    else res+=maxleft-A[left];
                    left++;
                }
                else{
                    if(A[right]>=maxright) maxright= A[right];
                    else res+=maxright-A[right];
                    right--;
                }
            }
            return res;
        }
    };
    
    
# https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.   
public int trap(int[] A){
    int a=0;
    int b=A.length-1;
    int max=0;
    int leftmax=0;
    int rightmax=0;
    while(a<=b){
        leftmax=Math.max(leftmax,A[a]);
        rightmax=Math.max(rightmax,A[b]);
        if(leftmax<rightmax){
            max+=(leftmax-A[a]);       // leftmax is smaller than rightmax, so the (leftmax-A[a]) water can be stored
            a++;
        }
        else{
            max+=(rightmax-A[b]);
            b--;
        }
    }
    return max;
}


# https://leetcode.com/problems/trapping-rain-water/discuss/17364/7-lines-C-C%2B%2B
# 使用level来记录柱子最左侧、最右侧的高度较小值；lower记录当前处理阶段两侧的较低柱高。
#   若较低柱高高于之前记录的最左和最后侧形成的level高，则level高度要更新
#   若低于，则较低柱高与 level之间形成可盛水的空间 (level - lower)
def trap(height):
    l, r = 0, len(height) - 1
    level, s  = 0, 0
    while l <= r:
        if height[l] < height[r]:
            lower = height[l]
            l += 1
        else:
            lower = height[r]
            r -= 1
        level = lower if lower > level else level 
        s += (level - lower)
    return s