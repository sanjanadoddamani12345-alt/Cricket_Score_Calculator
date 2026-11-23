
from main import (
    calculate_run_rate,
    calculate_strike_rate,
    calculate_required_runs,
    calculate_required_rate,
    predict_final_score,
    match_status
)


# Test 1: Calculate run rate
def test_run_rate():
    assert calculate_run_rate(150, 15) == 10


# Test 2: Run rate with zero overs
def test_run_rate_zero_overs():
    assert calculate_run_rate(100, 0) == 0


# Test 3: Calculate strike rate
def test_strike_rate():
    assert calculate_strike_rate(50, 25) == 200


# Test 4: Strike rate with zero balls
def test_strike_rate_zero_balls():
    assert calculate_strike_rate(50, 0) == 0


# Test 5: Calculate required runs
def test_required_runs():
    assert calculate_required_runs(180, 150) == 30


# Test 6: Calculate required run rate
def test_required_rate():
    assert calculate_required_rate(180, 150, 5) == 6


# Test 7: Predict final score
def test_predict_final_score():
    assert predict_final_score(150, 15, 20) == 200


# Test 8: Check match status
def test_match_status():
    assert match_status(180, 180) == "Target achieved! Match won."


# Test 9: Match still in progress
def test_match_in_progress():
    assert match_status(180, 150) == "Match is still in progress."
