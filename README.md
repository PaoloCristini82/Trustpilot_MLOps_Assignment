# Trustpilot MLOps Assignment

## *Requirements*:
1. Train a classifier that categorizes review sentences into positive, neutral and negative classes. We are less critical about the model you chose. So do not spend too much time on that. You can assume that each sentence inherits the rating of its parent review.
2. Deploy the trained model locally so that it can serve predictions with p99 latency of 300ms.
3. Not needed for this case, but ensure your solution can be easily deployed to a cloud environment.
4. Ensure appropriate logging and monitoring is in place.
5. Submit your solution via Github

## *Things to care about*
- Unit testing
- Readability (Code comments, etc)
- Thought Process
- Design Choices
- Performance Considerations
- Productionisation
- Extensibility and maintainability of a system

## Repo structure overview
### `/data`
Contains data for three distinct layers of processing, with the 'gold' layer serving as input for the model training process. `data_specs.md` provides details regarding fields for each layer.

### `/notebooks`
Includes interactive tools implemented as `.ipynb` files. `01_data_understanding.ipynb` is a mere exploration of the content of *bronze* layer, whilst `02_model_training.ipynb` runs definition, training and evaluation of the model

### `/scr`
Main directory for python code, further subdivided in:
 - `/scr/data`, where `data_pipeline.py` being useful for the transformations strictly linked to the development, while `data_preprocess.py` aimed to be used during productionisation too
  - `/scr/models`, where code for training, prediction, and evaluation is stored, as well as the `artifacts` directory, containing `.pkl` file(s) for models

### `/app`
Stores the ingredients for deploying a Flask application, via Dockerfile, providing prediction for a given "title+text" review

### `/tests`
Area where to store unit tests

## Design Choices

### Context
In order to translate "*Not needed for this case, but ensure your solution can be easily deployed to a cloud environment.*" into a plausible scenario it is possible to imagine a developer that mainly intends to have a framework to develop a model (the classifier), but at the same time provides the main ingredients to a potentially larger MLOps framework; specifically:
 - notebooks are used to provide interaction and governance of the different stages while developing, but the code which runs in the chunks is primarily a call to function kept in separated (and structured) modules. This approach streamline the development process, avoiding refactoring code
  - alongside a simple `flask` application for real time inferring, a docker file is provided in order to containerise it, and make it scalable within the production environment
  - a test of the correct functioning of the application is provided, which can be leveraged by a CI/CD pipeline/workflows, triggered by a pull request, whose positive outcome is a necessary condition for the subsequent merge

### Model
Although, according to the requirements, model choice should not be critical, it is actually quite important to briefly discuss about the implementation of the sought-after classifier. A key challenge is that the input data uses a '5-star' rating system (where apparently none of the rating can be 0) rather than a 3-class label: transforming 5-star ratings into "positive", "neutral", or "negative" would be quite controversial, as, notoriously, 5 is not a multiple of 3. Solution adopted has then been:
1. Applying min-max scaling to the labels to normalize them into a [0, 1] range
2. Training a regression model with a sigmoid activation to constrain predictions within the normalized label range, but treating the latter as a continuous variable which, *by chance*, appear to have just 5 different values
3. Predict a 'score' as a continuous variable.
4. Apply a 1/3-step division of the space to classify into the required 3 categories

For simplicity, attention has been paid just to fields `rating`, `title`, and `text`.

### Extensibility
Possible extensions for a stronger MLOps framework taste could be:
 - converting the notebooks into scheduled jobs (or single job with 2 tasks) that automatically retrain the model at a given frequency and/or when performance degrades below a certain threshold. In order to do that, developers may want to:
    - substitute main `/data` directory with more structured data support, external to the repository (databases, data lakes, etc..), and modify function `clean_data`
    - implement new sets of tests for data manipulation and model training (as the code would run now in production)
 - adopting a ML lifecycle management tool (like MLflow) to:
    - keep track of the different models (and versions) developed
    - enhance shareability of ML experiment within the developing team
- introducing `.yml` files, to govern CI/CD processes, in a dedicated folder (in case ML engineers want to use GitHub actions a specific directory is required anyway)
