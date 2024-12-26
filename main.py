import pickle
import streamlit as st

# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


# defining the function which will make the prediction using
# the data which the user inputs
def prediction(battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi):
    prediction = classifier.predict(
        [[battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Mobile Price Classification")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """ 
	<div style ="background-color:yellow;padding:13px"> 
	<h1 style ="color:black;text-align:center;">Streamlit Mobile Price Classifier ML App </h1> 
	</div> 
	"""

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    battery_power = st.number_input("Battery Power", value=0)
    blue = st.number_input("Bluetooth (0 or 1)", value=0)
    clock_speed = st.number_input("Clock Speed", value=0.0)
    dual_sim = st.number_input("Dual SIM (0 or 1)", value=0)
    fc = st.number_input("Front Camera MP", value=0)
    four_g = st.number_input("4G (0 or 1)", value=0)
    int_memory = st.number_input("Internal Memory (GB)", value=0)
    m_dep = st.number_input("Mobile Depth (cm)", value=0.0)
    mobile_wt = st.number_input("Mobile Weight (grams)", value=0)
    n_cores = st.number_input("Number of Cores", value=0)
    pc = st.number_input("Primary Camera MP", value=0)
    px_height = st.number_input("Pixel Height", value=0)
    px_width = st.number_input("Pixel Width", value=0)
    ram = st.number_input("RAM (MB)", value=0)
    sc_h = st.number_input("Screen Height", value=0)
    sc_w = st.number_input("Screen Width", value=0)
    talk_time = st.number_input("Talk Time (hours)", value=0)
    three_g = st.number_input("3G (0 or 1)", value=0)
    touch_screen = st.number_input("Touch Screen (0 or 1)", value=0)
    wifi = st.number_input("WiFi (0 or 1)", value=0)
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi)
        st.success('The output is {}'.format(result))

if __name__ == '__main__':
    main()
