class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for index, bar in enumerate(heights):
            #print("line 4, index", index)
            #print("line 5, bar", bar)
            print("")
            for index_2, bar_2 in enumerate(heights):

               # vertical = bar if bar < bar_2 else bar_2
                vertical = min(bar,bar_2)
                horizontal = abs(index - index_2)

                area = vertical * horizontal

                if area > max_area:
                    max_area = area
                   
        return(max_area)


        # O(n)
        # O(n^2)
