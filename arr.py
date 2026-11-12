def main():
    scores=[78,85,90,66,88]
    total= sum(scores)
    average= total/len (scores)
    print("== main/ masters brtanch output ===")
    print(f"scores: {scores}")
    print(f"sum:{total}")
    print(f"Average: {average}")
    print("\n== local branch output (max&min)==")
    print(f"maximum: {max(scores)}")
    print(f"minimum: {min(scores)}")