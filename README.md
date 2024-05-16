# Presentation Helper: Your AI-powered Speech Coach

This project is a presentation helper tool that leverages speech recognition and large language models (LLMs) to empower you to craft compelling and impactful presentations.

## Features

- **Speech Recognition**: Capture your presentation ideas and outline through voice input using your microphone.
- **LLM-powered Advice**: Analyze your speech content with an LLM to receive tailored suggestions for improvement. The LLM can identify areas like clarity, structure, engagement, and more.
- **Improved Efficiency**: Streamline the preparation process by dictating your thoughts instead of typing them out.

## Benefits

- **Boost Clarity and Structure**: Gain valuable insights into how well your presentation flows and how to structure it effectively.
- **Enhance Audience Engagement**: Receive guidance on how to make your presentation more engaging and connect with your audience on a deeper level.
- **Save Time and Effort**: Dictation allows for faster input compared to traditional typing.

## Getting Started

### Prerequisites

- Python 3.x
- use env.yml to download packages needed

### Installation

1. Install the required libraries using `conda env create -f environment.yml`.
2. Set up your LLM API access by getting a Google Gemini API key.
3. Create a .env file outside of the src folder and format the .env like this
```bash
API_KEY="INSERT-YOUR-API-KEY-HERE"
```

### Usage

1. Run the application script (`python run.py`) in the terminal in the src folder.
2. Follow the prompts to allow microphone access and speak about your presentation.
3. The tool will analyze your speech using the LLM and provide suggestions for improvement.

## Future Enhancements

- **AI-powered Slide Generation**: Explore the possibility of using the LLM to generate draft slides based on your speech input.
- **Voice Synthesis Feedback**: Consider incorporating AI voice synthesis to provide spoken feedback on your presentation delivery.
- **Visualizations**: Implement charts or graphs to represent the LLM's analysis of your speech content.

## Contributing

We welcome contributions from the community! Feel free to fork the repository, propose improvements, and submit pull requests.


## Disclaimer

The effectiveness of the LLM advice depends on the quality of the chosen LLM and the clarity of your speech input. Use this tool as a helpful guide, but maintain your own creative control over your presentations.
