# TASK 1: Score Counter
def score_counter(score_list):
    negative, neutral, positive = 0, 0, 0
    for score in score_list:
        if score <= 5:
            negative += 1
        elif score <= 8:
            neutral += 1
        else:
            positive += 1
    print(f"Negative: {negative}\nNeutral: {neutral}\nPositive: {positive}")

# TASK 2: ID Validator
def id_validator(verified_ids, feedback_ids):
    unverified = 0
    for id in feedback_ids:
        if id not in verified_ids:
            unverified += 1
    percent = (unverified / len(feedback_ids)) * 100
    print(f"{unverified} of {len(feedback_ids)} IDs unverified.")
    print(f"{percent}% unverified.")

# TASK 3: Nested Loop
def purchases_100(sales):
    count = 0
    for customer in sales:
        total = sum(customer) # İç döngü mantığı: listenin toplamı
        if total >= 100:
            count += 1
    return count

# TEST ALANI (Çalıştırmak için)
puanlar = [2, 7, 10, 5, 8, 9]
score_counter(puanlar)
