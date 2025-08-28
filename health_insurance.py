import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DATA_URL = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"

data = pd.read_csv(DATA_URL)
data = pd.get_dummies(data, drop_first=True)

X = data.drop("charges", axis=1)
y = data["charges"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model Trained Successfully!")

def predict_cost(age, bmi, children, smoker, sex, region):
    d = {
        'age': age,
        'bmi': bmi,
        'children': children,
        'sex_male': 1 if sex.lower() == "male" else 0,
        'smoker_yes': 1 if smoker.lower() == "yes" else 0,
        'region_northwest': 1 if region.lower() == "northwest" else 0,
        'region_southeast': 1 if region.lower() == "southeast" else 0,
        'region_southwest': 1 if region.lower() == "southwest" else 0,
    }
    input_df = pd.DataFrame(d, index=[0])
    return model.predict(input_df)[0]

if __name__ == "__main__":
    print("\n--- Health Cost Calculator ---")
    age = int(input("Enter Age: "))
    bmi = float(input("Enter BMI: "))
    children = int(input("Enter Number of Children: "))
    sex = input("Enter Sex (male/female): ")
    smoker = input("Smoker? (yes/no): ")
    region = input("Region (northeast/southeast/southwest/northwest): ")

    cost = predict_cost(age, bmi, children, smoker, sex, region)
    print(f"\nEstimated Health Insurance Cost: ${cost:.2f}")
