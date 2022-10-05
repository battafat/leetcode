class Solution:
    def maxArea(self, heights: List[int]) -> int:
        for index, bar in enumerate(heights):
            #print("line 4, index", index)
            #print("line 5, bar", bar)
            print("")
            for index_2, bar_2 in enumerate(heights):
                print("index", index)
                print("bar", bar)
                print("index_2", index_2)
                print("bar_2", bar_2)

                vertical = bar if bar < bar_2 else bar_2
                horizontal = abs(bar - bar_2)
                area = vertical * horizontal
                print("area", area)
                print("")
