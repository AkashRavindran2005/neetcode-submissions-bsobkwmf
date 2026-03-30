class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ''
        for i in strs:
            encode_str += str(len(i)) + '#' + i
        return encode_str 
    def decode(self, s: str) -> List[str]:
        decode_list = []
        j = 0
        while j <= s.count('#'):
            length = s.index('#') - 1
            i = s.index('#') + 1
            decode_list.append(s[i : i+int(s[length])])
            s = s.replace(s[length] + '#' + s[i:i+int(s[length])], '')
            j += 1
        return decode_list
            

