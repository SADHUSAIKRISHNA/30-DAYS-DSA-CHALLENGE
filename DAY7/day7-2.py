class Solution(object):
    def compress(self, chars):
        write, read = 0, 0
        while read < len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write


sol = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
length = sol.compress(chars)
print("Compressed List:", chars[:length])