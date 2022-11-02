from random import random
from concurrent.futures import ProcessPoolExecutor


def trial_run_5_3_score(param: float):
    """
    Performs a trial run with the std library random engine

    Returns
    n_pts_A: Final number of points to Alice
    n_pts_B: Final number of points to Bob
    flag_53: whether the 5-3 score ocurred in any point of the game

    Parameters:
    -----------
    param: float
        number between 0 and 1 which represents the first throw
    """

    n_pts_A: int = 0
    n_pts_B: int = 0
    flag_53: bool = False

    while (n_pts_A < 6 and n_pts_B < 6):

        if (random() > param):
            n_pts_A += 1

        else:
            n_pts_B += 1

        if (n_pts_A == 5 and n_pts_B == 3):
            flag_53 = True

    return n_pts_A, n_pts_B, flag_53


def uniform_random_generator(n: int):
    """
    Uniform random number generator that stops after n steps
    """
    for i in range(n):
        yield random()


def test_bobs_luck(n_trials: int):
    """
    Performs n_trials of the game

    Returns:
    n_A_wins: Number of games won by Alice
    n_B_wins: Number of games won by Bob 
    n_B_wins_with_5_3_score: Number of games where Bob won after a 5-3 score 
    n_53_score: Number of games where the 5-3 score happened
    """

    n_B_wins_with_5_3_score: int = 0
    n_B_wins: int = 0
    n_A_wins: int = 0
    n_53_score: int = 0

    rng = uniform_random_generator(n_trials)

    # Executing games in parallel to speed up process
    with ProcessPoolExecutor() as executor:
        it = executor.map(trial_run_5_3_score, rng, chunksize=10000)

        for idx, (n_A, n_B, flag_53) in enumerate(it):

            if n_B == 6:
                n_B_wins += 1

                if flag_53:
                    n_B_wins_with_5_3_score += 1
                    n_53_score += 1

            elif n_A == 6:
                n_A_wins += 1

                if flag_53:
                    n_53_score += 1

            else:
                raise ValueError("Oops, some error happened. Nobody has won the game!")

            print(f"{100 * idx / n_trials:.2f} % done", end="\r")

        print("---- All done ----")

    return n_A_wins, n_B_wins, n_B_wins_with_5_3_score, n_53_score


if __name__ == '__main__':

    n_total = 2000000
    n_A_wins, n_B_wins, n_B_wins_with_5_3_score, n_53_score = test_bobs_luck(n_total)
    print(f"P(Bob wins | 5-3 score) = {n_B_wins_with_5_3_score / n_53_score:.5f}")
