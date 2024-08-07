class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        in_octet = 0
        idx = 0
        for binary in data:
            binary_str =  f'{binary:08b}'
            if idx == in_octet:
                idx = 0
                in_octet = 0

            if not in_octet:
                if binary_str[0] == "0":
                    in_octet = 1
                elif binary_str[:3] == "110":
                    in_octet = 2
                elif binary_str[:4] == "1110":
                    in_octet = 3
                elif binary_str[:5] == "11110":
                    in_octet = 4
                else:
                    return False
                idx = 1
            else:
                if in_octet == 2 or in_octet == 3 or in_octet == 4:
                    if binary_str[:2] == "10":
                        idx += 1
                    else:
                        return False
                else:
                    return False
        return idx == in_octet