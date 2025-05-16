
def command(CT, Q):
    rail = [['\n' for i in range(len(CT))] for j in range(Q)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(CT)):
        if row == 0:
            dir_down = True
        if row == Q - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        row += 1 if dir_down else -1

    index = 0
    for i in range(Q):
        for j in range(len(CT)):
            if rail[i][j] == '*' and index < len(CT):
                rail[i][j] = CT[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(CT)):
        if row == 0:
            dir_down = True
        if row == Q - 1:
            dir_down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        row += 1 if dir_down else -1

    return "".join(result)

pookie = "AHRIOANIDUA!NTE_ABTHL_GI_RCE_O_EH!ORB_EATKYY!"
const = 3

patootie = command(pookie.replace(" ", ""), const)
print(patootie)
