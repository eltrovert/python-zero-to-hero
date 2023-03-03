row1 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️","⬜️","️⬜️","️⬜️"]
row4 = ["⬜️","️⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row5 = ["⬜️","⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
row6 = ["⬜️️","⬜️️","⬜️️","⬜️","️⬜️","️⬜️"]
map = [row1, row2, row3, row4, row5, row6]
print(f"{row1}\n{row2}\n{row3},{row4}\n{row5}\n{row6}")
position = input("Where do you want to put the treasure? ")

horizontalCoordinate = int(position[0]) - 1
verticalCoordinate = int(position[1]) - 1

map[verticalCoordinate][horizontalCoordinate] = "X"

print(f"{row1}\n{row2}\n{row3},{row4}\n{row5}\n{row6}")

