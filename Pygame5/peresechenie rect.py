class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.points = [(x, y), (x + w, y), (x, y + h), (x + w, y + h)]

    def intersect(self, rect):
        # for point in rect.points:
        #     if (self.x <= point[0] <= self.x + self.w) and (self.y <= point[1] <= self.y + self.h):
        #         return True
        # return False
        return (max(self.x, rect.x) <= min(self.x + self.w, rect.x + rect.w)) and (
                    max(self.y, rect.y) <= min(self.y, self.h, rect.y, rect.h))


rect1 = Rect(*map(int, input().split()))
rect2 = Rect(*map(int, input().split()))
if rect1.intersect(rect2) or rect2.intersect(rect1):
    print('YES')
else:
    print('NO')
