import preprocessing_functions as pf
import config

# ================================================
# TRAINING STEP - IMPORTANT TO PERPETUATE THE MODEL

# Load data
data = pf.load_data(config.PATH_TO_DATASET)


# Divide data set
X_train, X_test, y_train, y_test = pf.divide_train_test(data, config.TARGET)


# Get first letter from cabin variable
X_train['cabin'] = pf.extract_cabin_letter(X_train, 'cabin')

# Impute categorical variables
for var in config.CATEGORICAL_VARS:
    X_train[var] = pf.impute_na(X_train, var)

# Impute numerical variables
for var in config.NUMERICAL_TO_IMPUTE:
    X_train[var] = pf.add_missing_indicator(X_train, var)

# Group rare labels
for var in config.CATEGORICAL_VARS:
    X_train[var] = pf.remove_rare_labels(X_train, var, config.FREQUENT_LABELS[var])

# Encode categorical variables
for var in config.CATEGORICAL_VARS:
    X_train = pf.encode_categorical(X_train, var)


# check all dummies were added
X_train = pf.check_dummy_variables(X_train, config.DUMMY_VARIABLES)


# train scaler and save
scaler = pf.train_scaler(X_train, config.OUTPUT_SCALER_PATH)


# scale train set
X_train = pf.scale_features(X_train, config.OUTPUT_SCALER_PATH)


# train model and save
pf.train_model(X_train, y_train, config.OUTPUT_MODEL_PATH)


print('Finished training')