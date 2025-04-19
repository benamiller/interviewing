

if __name__ == "__main__":
    people = list(map(str, input().strip().split()))
    
    people_scores = {person: [] for person in people}
    
    print(people_scores)
