from model import PassFailModel

model = PassFailModel()

def menu():
    print("\n--- Pass Fail Predictor ---")
    print("1 Train Model")
    print("2 Accuracy")
    print("3 Predict Student")
    print("4 Generate Plot")
    print("5 Exit")

if not model.load_data():
    exit()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice=="1":
        model.train()
        print("Model trained successfully")

    elif choice=="2":
        if model.model is None:
            print("Train model first")
        else:
            acc = model.evaluate()
            print("Accuracy:", round(acc*100,2),"%")

    elif choice=="3":
        if model.model is None:
            print("Train model first")
            continue

        try:
            m = float(input("Math score: "))
            r = float(input("Reading score: "))
            w = float(input("Writing score: "))
        except:
            print("Invalid input")
            continue

        res = model.predict(m,r,w)
        print("Prediction:",res)

    elif choice=="4":
        model.generate_plot()
        print("Histogram saved as histogram.png")

    elif choice=="5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")