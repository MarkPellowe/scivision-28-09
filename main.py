from scivision import default_catalog, load_pretrained_model
# Get the model repo url
models_catalog = default_catalog.models.to_dataframe()
model_repo = models_catalog[models_catalog.name == "image-classifiers"].url.item()
model_repo 
model_repo = models_catalog[models_catalog.name == "image-classifiers"].url.item()
cat_dog_classifier = load_pretrained_model(model_repo,model="catdogclassifier")

