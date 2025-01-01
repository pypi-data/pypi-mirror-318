import csv
import numpy as np
import math

def entropy(data):
    counts = np.unique(data, return_counts=True)[1]
    probabilities = counts / len(data)
    return -np.sum(probabilities * np.log2(probabilities))

def info_gain(data, feature_index, target_index):
    total_entropy = entropy(data[:, target_index])
    values, counts = np.unique(data[:, feature_index], return_counts=True)
    subset_entropy = sum((counts[i] / len(data)) * entropy(data[data[:, feature_index] == v][:, target_index]) 
                         for i, v in enumerate(values))
    return total_entropy - subset_entropy

def build_tree(data, features, target_index):
    if len(np.unique(data[:, target_index])) == 1:
        return data[0, target_index]
    if len(features) == 0:
        return np.bincount(data[:, target_index].astype(int)).argmax()
    gains = [info_gain(data, i, target_index) for i in range(len(features))]
    best_feature_index = np.argmax(gains)
    tree = {features[best_feature_index]: {}}
    for value in np.unique(data[:, best_feature_index]):
        subtree = build_tree(
            np.delete(data[data[:, best_feature_index] == value], best_feature_index, axis=1),
            np.delete(features, best_feature_index), target_index - 1)
        tree[features[best_feature_index]][value] = subtree
    return tree

def classify(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    return classify(tree[feature][sample[feature]], sample)

with open("tennisdata.csv") as f:
    data = np.array(list(csv.reader(f)))

header, data = data[0], data[1:]
target_index, features = len(header) - 1, header[:-1]
tree = build_tree(data, features, target_index)

print("Decision Tree:", tree)
sample = {"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "High", "Windy": "False"}
print("Prediction for new sample:", classify(tree, sample))
