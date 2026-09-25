from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

iris = load_iris()
x = iris.data
y = iris.target

x_train , x_test , y_train , y_test = train_test_split(
    x , y , test_size = 0.2 , stratify = y
)

model = Pipeline([
    ("scaler" , StandardScaler()),
    ("classifier" , LogisticRegression(max_iter = 200))
])

model.fit(x_train , y_train)

predictions = model.predict(x_test)

accuracy = accuracy_score(y_test , predictions)

print("Model accuracy: ", accuracy)

joblib.dump({
    "model" : model,
    "target_names" : iris.target_names.tolist(),
    "feature_names" : iris.feature_names
}
, "iris_model.pkl")

print("Model saved successfully as iris_model.pkl")
