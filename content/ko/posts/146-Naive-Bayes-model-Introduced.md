---
title: "Naive Bayes model Introduced"
date: 2024-05-27T20:23:31+09:00
slug: "146-Naive-Bayes-model-Introduced"
original_url: "https://memoryhub.tistory.com/146"
tistory_id: 146
draft: false
---

*The Naive Bayes model is a probabilistic machine learning algorithm used for classification tasks. It is based on Bayes' Theorem, assuming strong independence (naive) among features.*

### The Big Picture

Imagine you are a detective trying to solve a case by considering various pieces of evidence. Each piece of evidence gives you some clue about who the culprit might be. The Naive Bayes model works similarly by calculating probabilities based on different features (evidence) to classify an outcome (culprit).

### Core Concepts

1. **Bayes' Theorem**: A formula that describes how to update the probabilities of hypotheses when given evidence.
2. **Naive Independence Assumption**: Assumes that the presence (or absence) of a particular feature is independent of the presence (or absence) of any other feature, given the class variable.
3. **Probability Calculation**: Computes the probability of each class based on the given features and chooses the class with the highest probability.

### Detailed Walkthrough

#### Bayes' Theorem

Bayes' Theorem is the foundation of the Naive Bayes model. It is expressed as:

[ P(C|X) = \frac{P(X|C) \cdot P(C)}{P(X)} ]

Where:

- ( P(C|X) ) is the posterior probability of class ( C ) given feature ( X ).
- ( P(X|C) ) is the likelihood of feature ( X ) given class ( C ).
- ( P(C) ) is the prior probability of class ( C ).
- ( P(X) ) is the prior probability of feature ( X ).

#### Naive Bayes Classifier

The Naive Bayes classifier applies Bayes' Theorem with the naive assumption of conditional independence between every pair of features given the class variable.

1. **Training Phase**:

   - Calculate the prior probability for each class:  
     [ P(C\_k) = \frac{\text{Number of instances in class } C\_k}{\text{Total number of instances}} ]
   - Calculate the likelihood of each feature given each class:  
     [ P(X\_i|C\_k) = \frac{\text{Number of instances in class } C\_k \text{ with feature } X\_i}{\text{Number of instances in class } C\_k} ]
2. **Prediction Phase**:

   - For a new instance, compute the posterior probability for each class:  
     [ P(C\_k|X) \propto P(C\_k) \cdot \prod\_{i=1}^{n} P(X\_i|C\_k) ]
   - Choose the class with the highest posterior probability.

### Understanding Through an Example

Suppose you want to classify emails as "Spam" or "Not Spam" based on the presence of certain words.

1. **Training Data**:

   - Emails labeled as "Spam" or "Not Spam".
   - Features: presence of words like "buy", "discount", "hello", etc.
2. **Training Phase**:

   - Calculate prior probabilities:  
     [ P(\text{Spam}) = \frac{\text{Number of Spam emails}}{\text{Total number of emails}} ]  
     [ P(\text{Not Spam}) = \frac{\text{Number of Not Spam emails}}{\text{Total number of emails}} ]
   - Calculate likelihoods for each word given the class.
3. **Prediction Phase**:

   - For a new email, extract features (words).
   - Calculate posterior probabilities for "Spam" and "Not Spam".
   - Classify the email based on the higher posterior probability.

#### Example in Python

Here is a simplified implementation of the Naive Bayes classifier for binary classification:

```
import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        self.classes, class_counts = np.unique(y, return_counts=True)
        self.priors = class_counts / y.shape[0]
        self.likelihoods = {c: {} for c in self.classes}

        for c in self.classes:
            X_c = X[y == c]
            for feature in range(X.shape[1]):
                feature_vals, feature_counts = np.unique(X_c[:, feature], return_counts=True)
                self.likelihoods[c][feature] = {val: count / X_c.shape[0] for val, count in zip(feature_vals, feature_counts)}

    def predict(self, X):
        predictions = []
        for instance in X:
            posteriors = []
            for c in self.classes:
                prior = np.log(self.priors[self.classes == c][0])
                likelihood = 0
                for feature in range(len(instance)):
                    val = instance[feature]
                    if val in self.likelihoods[c][feature]:
                        likelihood += np.log(self.likelihoods[c][feature][val])
                    else:
                        likelihood += np.log(1e-6)  # Smoothing for unseen feature values
                posterior = prior + likelihood
                posteriors.append(posterior)
            predictions.append(self.classes[np.argmax(posteriors)])
        return predictions

# Example usage
X_train = np.array([[1, 0], [1, 1], [0, 0], [0, 1]])
y_train = np.array([0, 0, 1, 1])
X_test = np.array([[1, 0], [0, 1]])

nb = NaiveBayes()
nb.fit(X_train, y_train)
print(nb.predict(X_test))  # Output might be: [0, 1]
```

### Conclusion and Summary

The Naive Bayes model is a straightforward and effective classification algorithm that relies on Bayes' Theorem and the naive assumption of feature independence. It is particularly useful for text classification and other applications where the independence assumption holds reasonably well.

### Test Your Understanding

1. What are the key assumptions made by the Naive Bayes classifier?
2. How does the Naive Bayes model handle continuous features?
3. Can you describe a real-world application where the Naive Bayes model might be useful?

### Reference

- "Pattern Recognition and Machine Learning" by Christopher M. Bishop
- [Scikit-learn: Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)
