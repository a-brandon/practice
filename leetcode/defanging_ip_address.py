class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = []
        for character in address:
            if character == '.':
                s.append(character.replace(character, '[.]'))
            else:
                s.append(character)
        return ''.join(s)
