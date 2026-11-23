
def calculate_run_rate(runs, overs):
    if overs <= 0:
        return 0
    return runs / overs


def calculate_strike_rate(runs, balls):
    if balls <= 0:
        return 0
    return (runs / balls) * 100


def calculate_required_runs(target, current_runs):
    return max(0, target - current_runs)


def calculate_required_rate(target, current_runs, overs_remaining):
    runs_needed = calculate_required_runs(target, current_runs)

    if overs_remaining <= 0:
        return 0 if runs_needed == 0 else -1

    return runs_needed / overs_remaining


def predict_final_score(runs, overs_played, total_overs):
    if overs_played <= 0:
        return 0

    run_rate = calculate_run_rate(runs, overs_played)
    return round(run_rate * total_overs)


def match_status(target, current_runs):
    if current_runs >= target:
        return "Target achieved! Match won."
    return "Match is still in progress."


def main():
    print("===== CRICKET SCORE CALCULATOR =====")

    runs = int(input("Enter total runs scored: "))
    overs = float(input("Enter overs played: "))
    balls = int(input("Enter balls faced by batsman: "))
    total_overs = float(input("Enter total match overs (20 or 50): "))

    target = int(input("Enter target score: "))
    remaining = float(input("Enter overs remaining: "))

    print("\n===== MATCH STATISTICS =====")

    print("Run Rate:", round(calculate_run_rate(runs, overs), 2))

    print("Predicted Final Score:",
          predict_final_score(runs, overs, total_overs))

    print("Strike Rate:",
          round(calculate_strike_rate(runs, balls), 2))

    print("Runs Required:",
          calculate_required_runs(target, runs))

    print("Required Run Rate:",
          round(calculate_required_rate(target, runs, remaining), 2))

    print("Match Status:", match_status(target, runs))


if __name__ == "__main__":
    main()
