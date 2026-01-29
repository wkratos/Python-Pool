import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        sys.exit()
    else:
        scores = []
        for arg in sys.argv[1:]:
            scores.append(int(arg))
        total_scores = len(scores)
        highest_score = max(scores)
        lowest_score = min(scores)
        average_score = sum(scores) / total_scores

        print("Scores processed:", scores)
        print(f"Total players: {total_scores}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {average_score:.1f}")
        print(f"High score: {highest_score}")
        print(f"Low score: {lowest_score}")
        print(f"Score range: {highest_score - lowest_score}")
