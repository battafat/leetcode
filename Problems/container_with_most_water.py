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

#basically, the solution that is given by leet code starts with the greatest
#width and then finds the greatest height at that width by moving the shorter bar.
#I WAS WRONG: It doesn't find the greatest height at that width. It's just that
#the area can't be greater if the height stays the same (limited by the shorter bar)
#while the width decreases by one. So it's not the greateast possible area at that
#width. It's just that it's the only possible area that could be greater than the
#previous one.
#Moving the taller bar cannot increase the area since we're limited by the short bar.

#For every value of horizontal, you want to increase your vertical.

#Someone explained in comments of the solution:
#"To clarify: let's say we kept the shortest forever, what would happen? Well,
#j-i would decrease, and either we come across a taller block, which doesn't
#matter because our shorter one we kept only mattered, or we find a shorter one,
#in which case that one matters."

#Then it calculates the area and sets that as the max_area.
#Then it decreases the width by 1 to get the next greatest width and calculates
#the greatest height. Then it calculates the greatest area.
#It checks to see if this area is bigger than the max_area. If it is, it becomes
#max_area.
#Done this way, you only have to go through the list once because you are starting
#with the biggest width and working down.
#It's possible that a lesser width will yield a greater area because of an increase
#in height, which is why it checks that area against max_area each time.
#This is actually pretty clever!
        # O(n)
        # O(n^2)
