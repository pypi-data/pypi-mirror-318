def first():
    print("""import csv

# Function to load the CSV file
def loadCsv(filename):
    # Open and read the CSV file
    lines = csv.reader(open(filename, "rt"))
    # Convert lines into a dataset
    dataset = list(lines)
    
    # Return the dataset as a list
    return dataset

# Attributes list for the problem
attributes = ['Sky', 'Temp', 'Humidity', 'Wind', 'Water', 'Forecast']
print("Attributes:", attributes)

# Number of attributes
num_attributes = len(attributes)

# CSV file containing weather data
filename = "weather.csv"  # Make sure this file is saved in the same directory
dataset = loadCsv(filename)
print("\nDataset:", dataset)

# Target values (outcomes for each instance)
target = ['Yes', 'Yes', 'No', 'Yes']
print("\nTarget:", target)

# Initial hypothesis (most specific, starting with '0' for all attributes)
hypothesis = ['0'] * num_attributes
print("\nInitial Hypothesis:", hypothesis)

# Find-S algorithm
print("\nThe Hypothesis are:")
for i in range(len(target)):
    if target[i] == 'Yes':  # Only consider positive examples ('Yes')
        for j in range(num_attributes):
            if hypothesis[j] == '0':  # If attribute is unset, set it to current value
                hypothesis[j] = dataset[i][j]
            elif hypothesis[j] != dataset[i][j]:  # If it doesn't match, generalize with '?'
                hypothesis[j] = '?'
        print(f"{i+1} = {hypothesis}")

# Print the final hypothesis after processing all examples
print("\nFinal Hypothesis:")
print(hypothesis)
""")
    
def second():
    print("""import numpy as np
import pandas as pd

# Loading Data from a CSV File
data = pd.DataFrame(pd.read_csv('training_examples.csv'))

# Separating concept features from the Target column
concepts = np.array(data.iloc[:, 0:-1])  # Features (all columns except the last)
target = np.array(data.iloc[:, -1])      # Target (last column)

# Candidate Elimination Algorithm function
def learn(concepts, target):
    '''learn() function implements the learning method of the Candidate Elimination algorithm.
    Arguments:
    concepts - a NumPy array with all the features (concepts from the dataset)
    target   - a NumPy array with corresponding output values (target labels)
    '''
    
    # Initialize S0 with the first instance from concepts (specific hypothesis)
    specific_h = concepts[0].copy()
    print("Initialization of Specific Hypothesis (S0) and General Hypothesis (G0):")
    print("Specific Hypothesis:", specific_h)

    # Initialize General Hypothesis G0 to the most general hypothesis (all '?')
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("General Hypothesis:", general_h)

    # Iterate over all training instances
    for i, h in enumerate(concepts):
        # If the target is positive, generalize the specific hypothesis
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'  # Generalize specific_h
                    general_h[x][x] = '?'  # Generalize general_h

        # If the target is negative, specialize the general hypothesis
        if target[i] == "No":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]  # Specialize general_h
                else:
                    general_h[x][x] = '?'  # Retain generality if the attribute matches
                
        print(f"\nSteps of Candidate Elimination Algorithm {i + 1}:")
        print("Specific Hypothesis:", specific_h)
        print("General Hypothesis:", general_h)
    
    # Remove overly general hypotheses from the final general hypothesis set
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])

    # Return final specific and general hypotheses
    return specific_h, general_h

# Running the Candidate Elimination algorithm
s_final, g_final = learn(concepts, target)

# Final Output
print("\nFinal Specific Hypothesis:")
print(s_final)
print("\nFinal General Hypothesis:")
print(g_final)
""")
    
def third():
    print("""import pandas as pd
import numpy as np

dataset = pd.read_csv('playtennis.csv', names=['outlook', 'temperature', 'humidity', 'wind', 'class'])

def entropy(col):
    _, counts = np.unique(col, return_counts=True)
    return -sum((count / sum(counts)) * np.log2(count / sum(counts)) for count in counts)

def info_gain(data, feature, target="class"):
    total_entropy = entropy(data[target])
    vals, counts = np.unique(data[feature], return_counts=True)
    return total_entropy - sum((counts[i] / sum(counts)) * entropy(data[data[feature] == vals[i]][target]) for i in range(len(vals)))

def ID3(data, features, target="class"):
    if len(np.unique(data[target])) == 1: return data[target].iloc[0]
    if not features: return data[target].mode()[0]
    best_feature = max(features, key=lambda f: info_gain(data, f, target))
    return {best_feature: {v: ID3(data[data[best_feature] == v], [f for f in features if f != best_feature], target) for v in np.unique(data[best_feature])}}

def predict(query, tree):
    for feature, branches in tree.items():
        return predict(query, branches.get(query.get(feature))) if isinstance(branches.get(query.get(feature)), dict) else branches.get(query.get(feature))

queries = dataset.iloc[:14, :-1].to_dict(orient="records")
tree = ID3(dataset.iloc[:14], dataset.columns[:-1].tolist())
accuracy = sum(predict(q, tree) == t for q, t in zip(queries, dataset["class"][:14])) / 14 * 100
print("Tree:", tree, "\nAccuracy:", accuracy, "%")
""")
    
def fourth():
    print("""import numpy as np

# Sigmoid Activation Function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training Data (XOR problem as an example)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input
y = np.array([[0], [1], [1], [0]])  # Output (XOR)

# Hyperparameters
epochs = 10000
learning_rate = 0.1
input_layer_neurons = X.shape[1]  # Number of input features
hidden_layer_neurons = 4  # Number of neurons in hidden layer
output_layer_neurons = 1  # Single output neuron

# Initialize weights and biases
np.random.seed(42)
weights_input_hidden = np.random.rand(input_layer_neurons, hidden_layer_neurons)
weights_hidden_output = np.random.rand(hidden_layer_neurons, output_layer_neurons)
bias_hidden = np.random.rand(1, hidden_layer_neurons)
bias_output = np.random.rand(1, output_layer_neurons)

# Training the Neural Network
for epoch in range(epochs):
    # Forward Propagation
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)
    
    # Backpropagation
    output_error = y - predicted_output
    output_delta = output_error * sigmoid_derivative(predicted_output)
    
    hidden_layer_error = output_delta.dot(weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)
    
    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
    weights_input_hidden += X.T.dot(hidden_layer_delta) * learning_rate
    bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(hidden_layer_delta, axis=0, keepdims=True) * learning_rate

# Test the model (after training)
print("Final output after training:")
print(predicted_output)

# Show updated parameters
print("\nUpdated weights and biases after training:")
print("Weights from input to hidden layer:")
print(weights_input_hidden)
print("Weights from hidden to output layer:")
print(weights_hidden_output)
print("Biases for hidden layer:")
print(bias_hidden)
print("Biases for output layer:")
print(bias_output)
""")
    
def fifth():
    print("""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
X = data.data  # Features
y = data.target  # Labels

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the Naive Bayes classifier
model = GaussianNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')  # Use 'macro' for multi-class
recall = recall_score(y_test, y_pred, average='macro')        # Use 'macro' for multi-class

# Print metrics
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Sample prediction
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example feature values
predicted_class = model.predict(sample)
print(f"\nPredicted class for {sample}: {data.target_names[predicted_class[0]]}")
""")

def sixth():
    print("""from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

# Load the 20 newsgroups dataset
newsgroups = fetch_20newsgroups(subset='all')  # Load all categories

# Features and labels
X = newsgroups.data
y = newsgroups.target

# Convert text data into numerical feature vectors using CountVectorizer
vectorizer = CountVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.3, random_state=42)

# Initialize and train the Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro', labels=range(20))  # Macro average for multi-class
recall = recall_score(y_test, y_pred, average='macro', labels=range(20))  # Macro average for multi-class

# Print metrics
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=newsgroups.target_names))
""")
    
def seventh():
    print("""import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load Heart Disease dataset from UCI Repository using ucimlrepo
dataset = fetch_ucirepo(id=45)

# Extract features and target
X = dataset.data.features
y = dataset.data.targets.to_numpy().ravel()  # Convert to numpy array and flatten to 1D array

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Calculate metrics for multiclass classification
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=1)  # Handle undefined precision
recall = recall_score(y_test, y_pred, average='weighted', zero_division=1)  # Handle undefined recall

# Print the results
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
""")
    

def eighth():
    print("""import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Generate and Save a Random Dataset
np.random.seed(42)
data = {
    "Feature1": np.random.rand(100) * 100,  # Random numbers between 0 and 100
    "Feature2": np.random.rand(100) * 100
}
df = pd.DataFrame(data)
df.to_csv("kmeans_data.csv", index=False)
print("Data saved to 'kmeans_data.csv'.")

# Step 2: Load the Dataset
data = pd.read_csv("kmeans_data.csv")

# Step 3: Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(data)

# Step 4: Visualize the Clusters
plt.figure(figsize=(8, 6))
colors = ['red', 'blue', 'green']
for cluster in range(3):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Feature1'], cluster_data['Feature2'], 
                color=colors[cluster], label=f'Cluster {cluster}')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            color='yellow', marker='X', s=200, label='Centroids')

plt.title("K-Means Clustering")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.legend()
plt.grid()
plt.show()
""")
    
def ninth():
    print("""from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # Features (Sepal Length, Sepal Width, Petal Length, Petal Width)
y = iris.target  # Target classes (0, 1, 2 representing species)

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Initialize the k-Nearest Neighbors classifier
k = 3  # Number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)

# Step 4: Train the k-NN model
knn.fit(X_train, y_train)

# Step 5: Make predictions on the test set
y_pred = knn.predict(X_test)

# Step 6: Calculate and print the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of k-NN model: {accuracy * 100:.2f}%")

# Step 7: Print both correct and wrong predictions
print("\nCorrect predictions:")
for i in range(len(y_test)):
    if y_test[i] == y_pred[i]:
        print(f"Sample {i}: True Label = {y_test[i]}, Predicted Label = {y_pred[i]}")

print("\nWrong predictions:")
for i in range(len(y_test)):
    if y_test[i] != y_pred[i]:
        print(f"Sample {i}: True Label = {y_test[i]}, Predicted Label = {y_pred[i]}")
""")
    

def tenth():
    print("""import numpy as np
import matplotlib.pyplot as plt

# Locally Weighted Regression (Simplified)
def locally_weighted_regression(x, X, y, tau):
    weights = np.exp(-((X - x)**2) / (2 * tau**2))  # Gaussian weights
    weighted_sum = np.sum(weights * y)             # Weighted sum of y
    weight_total = np.sum(weights)                 # Sum of weights
    return weighted_sum / weight_total             # Weighted average

# Generate synthetic data
np.random.seed(42)
X = np.linspace(1, 10, 100)                        # Feature
y = 2 * X + np.random.normal(0, 2, X.shape)        # Target with noise

# Set tau (bandwidth parameter)
tau = 1.0

# Predict using LWR
predictions = [locally_weighted_regression(x, X, y, tau) for x in X]

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(X, y, label="Data Points", color="blue", alpha=0.6)
plt.plot(X, predictions, label="LWR Curve (tau=1.0)", color="red", linewidth=2)
plt.title("Locally Weighted Regression (Simplified)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
""")
    
