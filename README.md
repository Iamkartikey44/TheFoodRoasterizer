# TheFoodRoasterizer 👨‍🍳🔥
Welcome to **Roast Me Chef!!**, a fun and interactive web app that generates hilarious roasts of your meal images in the style of famous personalities like Gordon Ramsay and CarryMinati. This project uses Streamlit for the web interface, Google Generative AI for roast generation, Text-to-Speech for audio synthesis, and FFmpeg for video creation.

![TheFoodRoasterizer-](https://github.com/Iamkartikey44/TheFoodRoasterizer/assets/68707728/c888a1ec-5062-4294-889e-9ffdc5c4f122)

## Features

- **Upload Image:** Choose an image of your meal to be roasted.
- **Select Anger Level:** Adjust the intensity of the roast.
- **Choose Roaster:** Select from various roasters, including Gordon Ramsay and CarryMinati.
- **Generate Roast:** Get a personalized roast for your meal.
- **Share on Twitter:** Share your roast directly on Twitter.
- **Audio & Video:** Play the roast audio or generate a video with the roast.

## Instructions

1. **Upload an Image:** Choose an image of your meal.
2. **Set Anger Level:** Use the slider to select the desired anger level.
3. **Choose Your Roaster:** Select a roaster from the dropdown menu.
4. **Generate Roast:** Click the "Roast/Rate my meal, Chef!" button.
5. **Enjoy & Share:** Enjoy the roast and share it on Twitter if you like.

## Technologies Used

- **Streamlit:** For creating the interactive web interface.
- **Google Generative AI:** For generating roast content.
- **Text-to-Speech:** For synthesizing roast audio.
- **FFmpeg:** For creating videos from images and audio.

## Setup and Installation

### Prerequisites

- Python 3.x
- Streamlit
- PIL (Pillow)
- Google Generative AI
- FFmpeg
- Requests

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Iamkartikey44/TheFoodRoasterizer
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your Google Generative AI API key:
   - Obtain an API key from Google.
   - Create a `secrets.toml` file in the `.streamlit` directory with the following content:
     ```toml
     GOOGLE_API_KEY = "your_google_api_key_here"
     ```

4. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Usage

- **Upload Image:** Upload an image of your meal.
- **Select Anger Level:** Set the anger level to determine the intensity of the roast.
- **Choose Roaster:** Select the personality who will roast your meal.
- **Generate Roast:** Click the button to generate and display the roast.
- **Play Audio/Generate Video:** Use the sidebar to play the roast audio or generate a video.

## Connect

- [LinkedIn](https://www.linkedin.com/in/kartikey-tiwari-32bb90187/)
- [GitHub](https://github.com/Iamkartikey44)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to [Streamlit](https://streamlit.io/) for providing an awesome framework for building web apps.
- Thanks to Google Generative AI for their powerful API.

