class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        out = []

        for i, x in enumerate(prices):
            discounts = prices[i + 1:]
            j, num = 0, None

            while j < len(discounts):
                if discounts[j] <= x:
                    out.append(x - discounts[j])
                    break

                j += 1
            else:
                out.append(x)

        return out