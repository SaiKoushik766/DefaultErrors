import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import os

class PassFailModel:

    FILE = "data.txt"

    def __init__(self):
        self.df = None
        self.model = None
        self.X_test = None
        self.y_test = None

    def load_data(self):
        if not os.path.exists(self.FILE):
            print("Dataset file missing!")
            return False

        self.df = pd.read_csv(self.FILE)

        self.df["average"] = self.df[
            ["math score","reading score","writing score"]
        ].mean(axis=1)

        self.df["result"] = (self.df["average"] >= 40).astype(int)

        return True


    def split_data(self):
        X = self.df[["math score","reading score","writing score"]]
        y = self.df["result"]

        return train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )


    def train(self):
        X_train,X_test,y_train,y_test = self.split_data()

        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X_train,y_train)

        self.X_test = X_test
        self.y_test = y_test


    def evaluate(self):
        preds = self.model.predict(self.X_test)
        acc = accuracy_score(self.y_test,preds)
        return acc


    def predict(self,m,r,w):
        arr = np.array([[m,r,w]])
        result = self.model.predict(arr)[0]
        return "PASS" if result==1 else "FAIL"


    def generate_plot(self):
        plt.hist(self.df["average"], bins=20)
        plt.title("Average Score Distribution")
        plt.xlabel("Score")
        plt.ylabel("Students")
        plt.savefig("histogram.png")
        plt.close()