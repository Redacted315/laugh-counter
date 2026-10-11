from .app import Counter


def main() -> None:
    player1 = input("Player 1's name: ")
    player2 = input("Player 2's name: ")
    counter = Counter(player1, player2)
    counter.mainloop()
    

if __name__ == "__main__":
    main()