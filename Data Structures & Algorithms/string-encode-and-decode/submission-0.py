class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ''
        for i in strs:
            for j in i:
                encode_str += (j+'!')
            encode_str += '@' 
        return encode_str
    def decode(self, s: str) -> List[str]:
        decode_list = []
        decode_str = ''
        for j in s:
            if j.isalpha():
                decode_str += j
            elif j == '@':
                decode_list.append(decode_str)
                decode_str = ''
                continue
        return decode_list
