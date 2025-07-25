# Clickbait Detector

A machine learning-powered clickbait detection system with a Chrome extension interface and Flask API backend. This project uses ensemble methods to identify clickbait content with high accuracy, specifically designed to work with YouTube video titles.

## 🎯 Overview

The Clickbait Detector combines the power of multiple machine learning models to predict whether a given title is clickbait or legitimate content. The system features:

- **Machine Learning Backend**: Ensemble model combining Naive Bayes and Random Forest classifiers
- **RESTful API**: Flask-based API for real-time predictions
- **Chrome Extension**: Browser extension that automatically detects clickbait on YouTube
- **Feature Engineering**: Advanced text analysis including linguistic patterns, formatting, and statistical features

## 🏗️ Architecture

```
├── backend/                    # Machine learning and API backend
│   ├── api/                   
│   │   ├── main.py            # Flask API server
│   │   └── utils.py           # Prediction utilities
│   ├── data/                  
│   │   └── clickbait_title_classification.csv  # Training dataset (32k+ samples)
│   ├── models/                
│   │   ├── combined.joblib    # Ensemble model
│   │   ├── nb.joblib          # Naive Bayes model
│   │   ├── rf.joblib          # Random Forest model
│   │   └── gb.joblib          # Gradient Boosting model
│   └── notebooks/             
│       └── exploration.ipynb  # Data analysis and model training
├── frontend/                  # Chrome extension
│   ├── manifest.json          # Extension configuration
│   ├── popup.html/js/css      # Extension popup interface
│   └── scripts/               
│       └── content.js         # YouTube integration script
└── test/                      # Test suite
    └── test_predict.py        # Model prediction tests
```

## 🚀 Features

### Machine Learning Models
- **Naive Bayes Classifier**: Text-based feature analysis using TF-IDF vectorization
- **Random Forest Classifier**: Engineered feature analysis (title length, word count, formatting patterns)
- **Ensemble Method**: Weighted combination of both models for improved accuracy

### Feature Engineering
The system analyzes multiple aspects of titles:
- **Linguistic Features**: Question words, pronouns, punctuation patterns
- **Statistical Features**: Title length, word count, character distribution
- **Formatting Features**: Uppercase count, digit presence, quotation marks
- **Semantic Features**: Average word length, question mark presence

### Chrome Extension
- **Real-time Detection**: Automatically analyzes YouTube video titles
- **Visual Indicators**: Displays clickbait probability percentage
- **Non-intrusive**: Seamlessly integrates with YouTube's interface
- **Background Processing**: Efficient monitoring without performance impact

## 📊 Dataset

The model is trained on a comprehensive dataset of 32,000+ labeled titles:
- **Source**: `backend/data/clickbait_title_classification.csv`
- **Labels**: Binary classification (0: Non-clickbait, 1: Clickbait)
- **Quality**: Diverse range of content from news articles, videos, and social media

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- Chrome/Chromium browser
- Node.js (optional, for development)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Swiifts/clickbait-detector.git
   cd clickbait-detector
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask API server**
   ```bash
   cd backend/api
   python main.py
   ```
   The API will be available at `http://localhost:8000`

### Chrome Extension Setup

1. **Open Chrome Extensions page**
   - Navigate to `chrome://extensions/`
   - Enable "Developer mode"

2. **Load the extension**
   - Click "Load unpacked"
   - Select the `frontend` folder

3. **Verify installation**
   - The extension icon should appear in the toolbar
   - Visit any YouTube video to see clickbait detection in action

## 🔧 API Usage

### Health Check
```bash
GET http://localhost:8000/health
```

### Predict Clickbait
```bash
POST http://localhost:8000/predict
Content-Type: application/json

{
    "title": "You Won't Believe What Happened Next!"
}
```

**Response:**
```json
{
    "prediction": 1,
    "nb_probability": 0.892,
    "rf_probability": 0.756,
    "combined_probability": 0.824
}
```

## 🧪 Testing

Run the test suite to verify model functionality:

```bash
cd test
python test_predict.py
```

The test includes various title types:
- Technical content (non-clickbait)
- Scientific articles (non-clickbait)  
- Sensationalized titles (clickbait)

## 📈 Model Performance

The ensemble model combines:
- **Naive Bayes**: Optimized for text pattern recognition
- **Random Forest**: Effective for engineered feature analysis
- **Weighted Average**: 50% NB + 50% RF for balanced predictions

Key metrics from training:
- High precision for clickbait detection
- Balanced recall to minimize false negatives
- Robust performance across diverse content types

## 🔍 How It Works

### 1. Feature Extraction
When a title is submitted, the system extracts:
```python
features = {
    'title_length': len(title),
    'title_world_count': len(title.split()),
    'title_uppercase_count': sum(1 for c in title if c.isupper()),
    'digit_count': sum(1 for c in title if c.isdigit()),
    'has_number': any(c.isdigit() for c in title),
    'starts_with_question': title.startswith(tuple(questions)),
    'contains_question_mark': '?' in title,
    'contains_quotation': '"' in title,
    'contains_pronoun': any(pronoun in title for pronoun in pronouns),
    'average_word_length': average_word_length
}
```

### 2. Model Prediction
- **Text Vectorization**: TF-IDF transformation for NB model
- **Feature Array**: Structured features for RF model
- **Ensemble Scoring**: Weighted combination of probabilities

### 3. Browser Integration
- **Content Script**: Monitors YouTube page changes
- **Title Detection**: Identifies video title elements
- **Real-time Updates**: Updates display with clickbait probability

## 🛡️ Privacy & Security

- **Local Processing**: All analysis happens locally or on your controlled server
- **No Data Collection**: The extension doesn't store or transmit personal data
- **Minimal Permissions**: Only requires access to YouTube and localhost API

## 🚧 Development Status

**Current Version**: 0.1 (Beta)

**Implemented Features**:
- ✅ Core ML models (NB + RF ensemble)
- ✅ Flask API with health monitoring
- ✅ Chrome extension with YouTube integration
- ✅ Comprehensive test suite
- ✅ Feature engineering pipeline

**Upcoming Features**:
- 🔄 Language translation support
- 🔄 Enhanced popup interface
- 🔄 Additional social media platform support
- 🔄 Model retraining pipeline
- 🔄 Performance analytics dashboard

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Add tests for new features
- Update documentation for API changes
- Test extension functionality across Chrome versions

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For questions, issues, or contributions:
- **Issues**: [GitHub Issues](https://github.com/Swiifts/clickbait-detector/issues)
- **Documentation**: This README and inline code comments
- **API Reference**: Available endpoints documented above

## 🙏 Acknowledgments

- Dataset contributors for comprehensive clickbait/non-clickbait examples
- scikit-learn community for robust ML algorithms
- Chrome Extensions API for seamless browser integration
- Flask community for lightweight web framework

---

**Made with ❤️ for a better, less clickbaity internet**
