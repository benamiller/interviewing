def migratoryBirds(arr):
    bird_frequencies = {}

    for bird in arr:
        bird_frequencies[bird] = bird_frequencies.get(bird, 0) + 1

    highest_frequency = 0
    highest_frequency_bird_id = None

    for bird_id, frequency in bird_frequencies.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            highest_frequency_bird_id = bird_id
        elif frequency == highest_frequency:
            if bird_id < highest_frequency_bird_id:
                highest_frequency_bird_id = bird_id

    return highest_frequency_bird_id


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    print(migratoryBirds(arr))
