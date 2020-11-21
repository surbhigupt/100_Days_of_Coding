class Solution:
    def groupAnagrams(self, wordArr: List[str]) -> List[List[str]]:
        
        def key_gen(word):
            count_list = []
            for i in set(word):
                count_list.append(sum([1 for j in word if j==i]))
            return ''.join(j for j in sorted(word)) + ''.join(str(j) for j in sorted(count_list))

        word_dict = defaultdict(list)
        for word in wordArr:
            key = key_gen(word)
            if key in word_dict:
                word_dict[key].append(word)
            else:
                word_dict[key] = [word]

        output = []
        output = output + [word_dict[j] for j in word_dict]
        
        return output