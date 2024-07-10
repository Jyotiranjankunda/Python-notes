# KBC Program
questions = [
    ["Q1: Current Railway Minister of India is", ["A. Mamta Banarjee", "B. Ram Vilash", "C. Ashwini Yadav", "D. Piyush Goyal"], "c"],
    ["Q2: Which god is also known as ‘Gauri Nandan’?", ["A. Agni", "B. Indra", "C. Hanuman", "D. Ganesha"], "d"],
    ["Q3: What does not grow on tree according to a popular Hindi saying?", ["A. Money", "B. Flowers", "C. Leaves", "D. Fruits"], "a"],
    ["Q4: Which city is known as Pink City in India?", ["A. Banglore", "B. Mysore", "C. Jaipur", "D. Kochi"], "c"],
    ["Q4: Who wrote India's National Anthem?", ["A. Rabindranath Tagore", "B. Lal Bahadur Shastri", "C. Chetan Bhagat", "D. RK Narayan"], "a"],
]

prices = [100, 500, 1000, 5000, 7500]

# print(questions)
sum = 0
for ques in questions:
    print("")
    print(ques[0])
    for options in ques[1]:
        print(options)

    ans = input("Your answer : ")
    if(ans.lower() == ques[2]):
        print("Correct answer")
        sum += prices[questions.index(ques)]
        print(f"Your prize : {sum}")
    else:
        print("Wrong answer\nQuiz ended")
        print(f"Your prize : {sum}")
        break