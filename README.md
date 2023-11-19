# wine

wine-eda-and-backfill-feature-group.ipynb

  A feature pipeline notebook that preprocesses the wine quality dataset, visualize and exploratory analyse the attributes, and registers the dataset as a Feature Group with Hopsworks.


wine-training-pipeline.ipynb

  A training pipeline that reads training data with a Feature View from Hopsworks, trains a Decision Tree classifier model to predict if a wine’s quality. Register the model 
with Hopsworks.
  By contrast, we found that the accuaracy in Decision Tree algorithm is higher than in K-nearest-neighbors algorithm, so we chose Decision Tree algorithm as our classifier.


\huggingface-spaces-wine\wine\app.py

  A Gradio application that downloads our model from Hopsworks and provides a User Interface to allow users to enter or select feature values to predict the quality of a wine for the features you entered.


wine-feature-pipeline-daily.py

  A new “daily” feature pipeline that runs once per day to add a new synthetic wine, it contains a synthetic wine generator function.


wine-batch-inference-pipeline.py

  A batch inference pipeline to predict the quality of the new wine(s) added, and build a Gradio application to show the most recent wine quality prediction and outcome, and a confusion matrix with historical prediction performance.


public URL for the 2 Gradio Applications:

[https://huggingface.co/spaces/Antares28/wine](https://huggingface.co/spaces/Antares28/wine)
[https://huggingface.co/spaces/Antares28/wine_new](https://huggingface.co/spaces/Antares28/wine_new)
