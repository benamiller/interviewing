

if __name__ == "__main__":
    people = list(map(str, input().strip().split()))
    
    people_scores = {person: [] for person in people}
    
    for person in people:
        scores_for_person = list(map(int, input().strip().split()))
        people_scores[person] += scores_for_person

    query = input()
    print(people_scores)
    print(query)
