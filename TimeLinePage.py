import streamlit as st

# Custom CSS for styling the timeline and title
timeline_css = """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: blue;  /* Set background color to blue */
            color: white;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;  /* Centering the entire body content */
            height: 100vh;  /* Full screen height */
            text-align: center; /* Center text for entire body */
        }
        /* Importing a modern, futuristic font (Roboto) from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');

        .timeline-container {
            position: relative;
            width: 80%;
            margin: 30px auto;
            padding: 20px;
            text-align: center; /* Center the timeline container */
        }
        .timeline {
            position: absolute;
            left: 50%;
            height: 100%;
            width: 4px;
            background-color: #00ffcc;
            z-index: 1;
            transform: translateX(-50%);  /* Ensures timeline is centered */
        }
        .event {
            position: relative;
            margin: 25px 0; /* Increased space between events for desktop */
            text-align: left;  /* Align text to the left */
            z-index: 2;
            display: flex;
            justify-content: flex-start;  /* Align items to the left */
            align-items: center;  /* Align items vertically */
        }
        .circle {
            width: 70px;  /* Smaller circle size */
            height: 70px;  /* Smaller circle size */
            border-radius: 50%;
            background-color: #00ffcc;
            display: inline-block;
            margin-bottom: 30px;  /* More space below the circle */
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.6);
            transition: transform 0.3s ease;
            margin-left: 20px;  /* Position hexagon to the right */
        }
        .circle:hover {
            transform: scale(1.4); /* Bigger hover effect */
        }
        .event-content {
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 8px;
            padding: 80px;  /* Increased padding for more space around the text */
            margin-top: 20px;
            width: 600px;  /* Significantly larger width for better visibility */
            height: 600px;
            margin-left: 588px;  /* Center the box */
            box-shadow: 0 0 25px rgba(0, 255, 204, 0.6);
            transition: background-color 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: center;  /* Vertically center the content */
            text-align: center;  /* Center the text inside the event box */
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); /* Larger hexagonal shape */
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.5), 0 4px 6px rgba(0, 0, 0, 0.2); /* Shadow for 3D depth */
            transform: rotateX(10deg); /* Adds a slight 3D tilt */
        }
        .event-content:hover {
            background-color: rgba(0, 255, 204, 0.3);
        }
        .event-content h4 {
            font-size: 36px;  /* Larger header text */
            margin: 0;
            text-align: center;  /* Center the header */
            font-weight: bold;
        }
        .event-content p {
            font-size: 24px;  /* Larger paragraph text */
            margin-top: 15px;
            text-align: center;  /* Center the paragraph text */
        }
        .event-content a {
            color: #00ffcc;
            text-decoration: none;
            font-size: 24px;  /* Larger link text */
            font-weight: bold;
            margin-top: 20px;
            display: inline-block;
        }
        .event-content a:hover {
            text-decoration: underline;
        }
        .timeline-text {
            margin-top: 20px;
            color: #00ffcc;
            font-weight: bold;
            font-size: 20px;
        }
        /* Large title with Roboto font */
        h1 {
            font-family: 'Roboto', sans-serif;
            font-size: 100px;  /* Significantly larger title */
            margin-top: 40px;
            color: #000000;  /* Black color for the title */
            font-weight: bold;  /* Bold text */
            text-align: center;  /* Center the title */
            text-transform: uppercase;  /* Uppercase letters for the title */
            margin-bottom: 20px;  /* Space below the title */
        }
        /* Arrow styles */
        .arrow {
            width: 0;
            height: 0;
            border-left: 10px solid transparent;
            border-right: 10px solid transparent;
            border-top: 20px solid white; /* Downward arrow */
            position: absolute;
        }
        /* Positioning arrows on each side of the hexagon */
        .arrow-left {
            left: -20px;
            top: 45%;
        }
        .arrow-right {
            right: -20px;
            top: 45%;
        }
    </style>
"""

# Streamlit app
def main():
    st.set_page_config(page_title="Time Travel Timeline", layout="wide")
    st.markdown(timeline_css, unsafe_allow_html=True)

    # Display the new centered title with Roboto font
    st.markdown('<h1>Have a Goal, We Will Get You There</h1>', unsafe_allow_html=True)

    # Create a container for the timeline
    timeline = [
        {"date": "2024 - Present", "text": "Start of our time travel journey.", "link": "#", "color": "#00ffcc"},
        {"date": "2024 - March", "text": "Time to adjust our path and jump!", "link": "#", "color": "#ff007f"},
        {"date": "2024 - June", "text": "Another step forward in time.", "link": "#", "color": "#ff9800"},
        {"date": "2024 - September", "text": "We are getting closer to the future!", "link": "#", "color": "#2196f3"},
        {"date": "2025 - January", "text": "Almost there, only a few months left.", "link": "#", "color": "#9c27b0"},
        {"date": "2025 - May", "text": "The future is now!", "link": "#", "color": "#3f51b5"},
        {"date": "2025 - August", "text": "Time travel completed!", "link": "#", "color": "#8bc34a"},
    ]

    # Display the timeline
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    st.markdown('<div class="timeline"></div>', unsafe_allow_html=True)

    for event in timeline:
        st.markdown(f'<div class="event">', unsafe_allow_html=True)
        st.markdown(f'<div class="circle"></div>', unsafe_allow_html=True)  # Smaller circle
        # Add arrows to each side of the hexagon
        st.markdown(f'<div class="arrow arrow-left"></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="arrow arrow-right"></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="event-content" style="border-left: 5px solid {event["color"]};">'
                    f'<h4>{event["date"]}</h4><p>{event["text"]}</p></div>',
                    unsafe_allow_html=True)
        st.markdown(f'</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
