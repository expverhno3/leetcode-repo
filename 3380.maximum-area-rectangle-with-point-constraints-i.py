# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/description/

from typing import List, Tuple

class Solution:
    # Helper function to calculate the maximum rectangle area given four points
    def get(self, points: List[Tuple[int, int]]) -> int:
        maxArea = -1
        for i in range(len(points) - 3):
            # Check if these points can form a rectangle:
            # - First and second points have the same x-coordinate
            # - Third and fourth points have the same x-coordinate
            # - First and third points have the same y-coordinate
            # - Second and fourth points have the same y-coordinate
            if (points[i][0] == points[i + 1][0] and
                points[i + 2][0] == points[i + 3][0] and
                points[i][1] == points[i + 2][1] and
                points[i + 1][1] == points[i + 3][1]):
                # Calculate the area of the rectangle
                area = (points[i + 2][0] - points[i][0]) * \
                       (points[i + 1][1] - points[i][1])
                maxArea = max(maxArea, area)
        return maxArea

    def maxRectangleArea(self, points: List[List[int]]) -> int:
        maxArea = -1
        n = len(points)

        # Sort the points by their x-coordinates and then by y-coordinates
        points.sort()

        # Iterate over the points to find all potential rectangles
        for i in range(n - 3):
            rectanglePoints = []

            # Add the first two points of the rectangle
            rectanglePoints.append((points[i][0], points[i][1]))
            rectanglePoints.append((points[i + 1][0], points[i + 1][1]))

            # Find the next two points that complete the rectangle
            j = i + 2
            while j < n - 2:
                # Skip points that don't align with the y-coordinates of the rectangle
                if points[j][1] > points[i + 1][1] or points[j][1] < points[i][1]:
                    j += 1
                else:
                    break

            # Add the potential third and fourth points
            if j < n - 1:
                rectanglePoints.append((points[j][0], points[j][1]))
                rectanglePoints.append((points[j + 1][0], points[j + 1][1]))

                # Calculate the maximum area for this set of points
                maxArea = max(maxArea, self.get(rectanglePoints))

        return maxArea