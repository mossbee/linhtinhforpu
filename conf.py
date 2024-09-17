import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Ground truth and predicted labels
# y_true = [0] * 50 + [1] * 50
# y_pred = [0] * 49 + [1] + [0] * 2 + [1] * 48
y_true = [0] * 50 + [1] * 50
y_pred = [0] * 50 + [1] * 0 + [0] * 0 + [1] * 50

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1])
disp.plot(cmap=plt.cm.Blues)

# Save the confusion matrix as a PNG file
plt.savefig('confusion_matrix.png')
# plt.show()
