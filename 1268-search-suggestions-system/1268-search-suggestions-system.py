class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        result = []
        prefix = ""

        for ch in searchWord:
            prefix += ch

            left = 0
            right = len(products)

            while left < right:
                mid = (left + right) // 2
                if products[mid] < prefix:
                    left = mid + 1
                else:
                    right = mid

            suggestions = []

            for i in range(left, min(left + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break

            result.append(suggestions)

        return result