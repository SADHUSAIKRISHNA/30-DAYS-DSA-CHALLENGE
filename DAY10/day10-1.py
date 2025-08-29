class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen = set()        
        repeated = set()     

       
        for i in range(len(s) - 9):
            sequence = s[i:i+10]  
            print(f"Checking sequence from index {i} to {i+9}: {sequence}")
            
            if sequence in seen:
                print(f"Already seen: {sequence} → adding to repeated")
                repeated.add(sequence)
            else:
                print(f"First time seeing: {sequence} → adding to seen")
                seen.add(sequence)

        print("\nRepeated sequences found:")
        print(list(repeated))
        return list(repeated)

# Example 
dna = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
sol = Solution()
sol.findRepeatedDnaSequences(dna)