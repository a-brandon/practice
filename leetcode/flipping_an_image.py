class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        flipped_imgs = [b[::-1] for b in A]

        for img in flipped_imgs:
            for i, bit in enumerate(img):
                if bit == 0:
                    img[i] = 1
                else:
                    img[i] = 0

        return flipped_imgs