import pickle
import streamlit as st

# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


# defining the function which will make the prediction using
# the data which the user inputs
def prediction(
    battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory,
    m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram,
    sc_h, sc_w, talk_time, three_g, touch_screen, wifi
):
    inputs = [
        [
            int(battery_power), int(blue), float(clock_speed), int(dual_sim),
            int(fc), int(four_g), int(int_memory), float(m_dep), int(mobile_wt),
            int(n_cores), int(pc), int(px_height), int(px_width), int(ram),
            int(sc_h), int(sc_w), int(talk_time), int(three_g),
            int(touch_screen), int(wifi)
        ]
    ]
    prediction = classifier.predict(inputs)
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
    battery_power= st.text_input("battery_power", "Type Here")
    blue = st.text_input("blue", "Type Here")
    clock_speed = st.text_input("clock_speed", "Type Here")
    dual_sim = st.text_input("dual_sim", "Type Here")
    fc = st.text_input("fc", "Type Here")
    four_g = st.text_input("four_g", "Type Here")
    int_memory = st.text_input("int_memory", "Type Here")
    m_dep = st.text_input("m_dep", "Type Here")
    mobile_wt = st.text_input("mobile_wt", "Type Here")
    n_cores = st.text_input("n_cores", "Type Here")
    pc = st.text_input("pc", "Type Here")
    px_height = st.text_input("px_height", "Type Here")
    px_width = st.text_input("px_width", "Type Here")
    ram = st.text_input("ram", "Type Here")
    sc_h = st.text_input("sc_h", "Type Here")
    sc_w = st.text_input("sc_w", "Type Here")
    talk_time = st.text_input("talk_time", "Type Here")
    three_g = st.text_input("three_g", "Type Here")
    touch_screen = st.text_input("touch_screen", "Type Here")
    wifi = st.text_input("wifi", "Type Here")
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi)
    st.success('The output is {}'.format(result))

if __name__ == '__main__':
    main()
