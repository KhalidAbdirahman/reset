class SecretList(list):
    def __str__(self):
        if (len(self) == 0):
            return str([])
        else:
            return str(self[0])

# sec = SecretList()
# sec.append(79)
# sec.append(3)
# sec.append(0)

# print(str(sec))

