def main():
    """
    Call funtion to calculate conditional possibilities with Bayes Theorem
    """

    population = 276470345

    # These 3 variables are for the known probabilities.
    # Change them to see the effect on P(ill|positive)
    P_ill = 0.0806212326
    P_positive_if_ill = 0.94 # sensitivity
    P_negative_if_healthy = 0.98 # specificity

    print()

    calculate_with_bayes(P_ill, P_positive_if_ill, P_negative_if_healthy)


def calculate_with_bayes(P_ill, P_positive_if_ill, P_negative_if_healthy):

    """
    Calculate P(ill | positive) with Bayes' Theorem.
    """

    P_healthy = 1 - P_ill
    P_positive_if_healthy = 1 - P_negative_if_healthy
    P_ill_if_positive = (P_positive_if_ill * P_ill) / ((P_healthy * P_positive_if_healthy) + (P_ill * P_positive_if_ill))

    heading = "Calculate P(ill | positive) with Bayes' Theorem"
    print(heading)
    print("=" * len(heading) + "\n")

    print(f"P(ill):                 {P_ill}")
    print(f"P(healthy):             {P_healthy}")
    print(f"P(positive if ill):     {P_positive_if_ill}")
    print(f"P(positive if healthy): {P_positive_if_healthy:>.3f}\n")

    print("                                        P(positive if ill) * P(ill)")
    print("P(ill | positive) = -------------------------------------------------------------------")
    print("                      P(healthy) * P(positive if healthy) + P(ill) * P(positive if ill)")

    print("\n")

    print(f"                                               {P_positive_if_ill} * {P_ill}")
    print("                   = -------------------------------------------------------------------")
    print(f"                                         {P_healthy} * {P_positive_if_healthy:>.3f} + {P_ill} * {P_positive_if_ill}")

    print("\n")

    print(f"                   = {P_ill_if_positive:>.3f}")


main()
