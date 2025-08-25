from auth import signup, login
from blackjack import play_blackjack
from database import save_result, view_scores
from game_tracker import record_game, view_game_history, show_leaderboard

def normalize_outcome(result):
    result = result.lower().strip()

    # Handle common variations and phrasing
    if "you win" in result:
        return "Win"
    elif "dealer wins" in result:
        return "Lose"
    elif "draw" in result or "tie" in result or "it's a tie" in result:
        return "Draw"
    else:
        return "Unknown"

def main():
    print("🎲 Welcome to Blackjack!")

    while True:
        choice = input("1. Login\n2. Signup\nChoose (1 or 2): ").strip()
        if choice in {"1", "2"}:
            break
        print("⚠️ Invalid choice. Please enter 1 or 2.")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if choice == "1":
        if not login(username, password):
            print("❌ Invalid login. Exiting.")
            return
    else:
        signup_msg = signup(username, password)
        print(signup_msg)

    while True:
        print("\n📋 Menu:")
        print("1. Play Blackjack")
        print("2. View Scores")
        print("3. View Game History")
        print("4. Leaderboard")
        print("5. Exit")

        option = input("Choose (1-5): ").strip()

        if option == "1":
            result, p_score, d_score = play_blackjack()
            print(f"\n🃏 Result: {result}")

            outcome = normalize_outcome(result)
            if outcome == "Unknown":
                print("⚠️ Could not interpret game outcome. Game not recorded.")
                continue

            save_result(username, p_score, d_score, result)
            record_game(username, p_score, d_score, outcome)
            print("✅ Game recorded successfully.")

            again = input("Play again? (y/n): ").strip().lower()
            if again != "y":
                print("👋 Thanks for playing!")
                break

        elif option == "2":
            view_scores(username)

        elif option == "3":
            view_game_history(username)

        elif option == "4":
            show_leaderboard()

        elif option == "5":
            print("👋 Goodbye! Come back soon.")
            break

        else:
            print("⚠️ Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()