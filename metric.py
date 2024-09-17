import numpy as np
from sklearn.metrics import confusion_matrix

# Ground truth and predicted labels
# y_true = [0] * 50 + [1] * 50
# y_pred = [0] * 49 + [1] + [0] * 2 + [1] * 48
y_true = [0] * 50 + [0] * 50
y_pred = [0] * 50 + [0] + [0] * 0 + [0] * 50

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Extract TN, FP, FN, TP
tn, fp, fn, tp = cm.ravel()

# Calculate additional metrics
fpr = fp / (fp + tn)  # False Positive Rate
fnr = fn / (fn + tp)  # False Negative Rate

# Print the results
print(f'True Positives (TP): {tp}')
print(f'True Negatives (TN): {tn}')
print(f'False Positives (FP): {fp}')
print(f'False Negatives (FN): {fn}')
print(f'False Positive Rate (FPR): {fpr:.2f}')
print(f'False Negative Rate (FNR): {fnr:.2f}')
