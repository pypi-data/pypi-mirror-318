import numpy as np
import logging
import matplotlib.pyplot as plt
from .custom_exceptions import InvalidUserInputError

# logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Cache to avoid repeated predictions on the same sample
prediction_cache = {}

def plot_prediction(prediction):
    """Plot the prediction result using matplotlib."""
    plt.figure(figsize=(6, 4))
    plt.bar(range(len(prediction[0])), prediction[0])  # make sure / assume batch size of 1
    plt.title("Prediction Visualization")
    plt.xlabel("Classes")
    plt.ylabel("Prediction Value")
    plt.show()

def interactive_mode(model, X=None):
    """
    Run the interactive prediction mode.
    Args:
        model: Trained Keras model for predictions.
        X: Optional dataset for random sampling and predictions.
    """
    if model is None:
        logging.error("Model is not loaded. Cannot proceed with interactive mode.")
        return

    logging.info("Entering interactive mode. Type 'stop' to exit.")
    
    while True:
        try:
            if X is not None:
                # Randomly select a sample if dataset is provided
                sample_index = np.random.randint(0, X.shape[0])
                input_data = X[sample_index:sample_index + 1]  # batch of size 1
                
                # Check cache
                if sample_index in prediction_cache:
                    prediction = prediction_cache[sample_index]
                    logging.info(f"Using cached prediction for sample {sample_index}.")
                else:
                    prediction = model.predict(input_data)
                    prediction_cache[sample_index] = prediction
                    logging.info(f"Prediction for sample {sample_index}: {prediction}")

                # Plot the prediction
                plot_prediction(prediction)
            else:
                # For user input
                energy_level_input = input("Enter an energy level (or 'stop' to exit): ").strip().lower()
                if energy_level_input == "stop":
                    logging.info("Exiting interactive mode.")
                    break

                energy_level = float(energy_level_input)
                prediction = model.predict([[energy_level]])  # adjust input shape for the model
                logging.info(f"Prediction for energy level {energy_level}: {prediction}")

                # Plot the prediction
                plot_prediction(prediction)

            # User input for continuation
            user_input = input("Enter 'continue' for another prediction or 'stop' to exit: ").strip().lower()
            if user_input == "stop":
                logging.info("Exiting interactive mode.")
                break
            elif user_input == "continue":
                logging.info("Continuing to the next prediction.")
            else:
                raise InvalidUserInputError("Invalid input. Please type 'continue' or 'stop'.")
        except InvalidUserInputError as e:
            logging.warning(f"User input error: {e}")
            continue
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            break
