from phishing_domain_detection.constant.training_pipeline import SAVED_MODEL_DIR
from phishing_domain_detection.ml.model.estimator import ModelResolver
from phishing_domain_detection.utils.main_utils import load_object
from features import extract_features
import streamlit as st
import pandas as pd


def load_prediction(input_data):

    # Convert JSON to DataFrame Using read_json()
    df = pd.DataFrame(input_data, index=[0])
    model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
    if not model_resolver.is_model_exists():
        return "Model is not available."
    best_model_path = model_resolver.get_best_model_path()
    model = load_object(file_path=best_model_path)
    prediction = model.predict(df)
    return prediction

    
# Create a dataframe with extracted features
        
columns = ['qty_dot_url','qty_hyphen_url','qty_underline_url','qty_slash_url','qty_tld_url','length_url','qty_dot_domain','qty_hyphen_domain','qty_vowels_domain','domain_length','qty_dot_directory','qty_hyphen_directory','qty_underline_directory','qty_slash_directory','qty_questionmark_directory','qty_equal_directory','qty_at_directory','qty_and_directory','qty_exclamation_directory','qty_space_directory','qty_tilde_directory','qty_comma_directory','qty_plus_directory','qty_asterisk_directory','qty_hashtag_directory','qty_dollar_directory','qty_percent_directory','directory_length','qty_dot_file','qty_hyphen_file','qty_underline_file','qty_slash_file','qty_questionmark_file','qty_equal_file','qty_at_file','qty_and_file','qty_exclamation_file','qty_space_file','qty_tilde_file','qty_comma_file','qty_plus_file','qty_asterisk_file','qty_hashtag_file','qty_dollar_file','qty_percent_file','file_length','qty_dot_params','qty_underline_params','qty_equal_params','qty_and_params','qty_tilde_params','qty_plus_params','qty_dollar_params','params_length','time_response','domain_spf','asn_ip','time_domain_activation','time_domain_expiration','qty_ip_resolved','qty_nameservers','qty_mx_servers','ttl_hostname','tls_ssl_certificate','qty_redirects','url_shortened']

# Define the Streamlit app


def main():

    # Set the page title
    st.set_page_config(page_title='Phishing Domain Detection')

    # title
    st.title(':sleuth_or_spy: **:orange[_PHISHING DOMAIN DETECTION_]** :sleuth_or_spy:')
    st.text("")
    st.text("")

    try:
        st.text("")
        st.markdown("<h1 style='color: #90EE90; font-size: 20px;'>Let's Check Whether URL is a Legitimate Website or a Phishing Website!</h1>", unsafe_allow_html=True)
        st.text("")
        st.text("")
        # Add a text input for the user to enter the URL
        url = st.text_input(":point_down: **:blue[Enter Your URL in Search Box]** :point_down:")
        # Add a button to make the prediction
        if st.button("**:green[Check]**"):

            # Extract the features from the URL
            features = extract_features(url)
            print(features, "length of features: ", len(features))

            input_data = dict(zip(columns, features))
            print(input_data)

            prediction = load_prediction(input_data)
         
            # Display the prediction
            if prediction[0] == 0:
                st.success('The URL is Legitimate!')
                print(0)
            else:
                st.error('The URL is a Phishing Attempt!')
                print(1)

    except Exception as e:
        st.text(e)


if __name__ == "__main__":
    main()
