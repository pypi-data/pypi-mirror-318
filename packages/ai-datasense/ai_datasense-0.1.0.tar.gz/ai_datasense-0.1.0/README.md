🚀 AI DataSense
AI-powered data insights, anomaly detection, and visualization across diverse data formats.

📖 Overview
AI DataSense is an AI-driven Python package designed to seamlessly analyze data, detect anomalies, generate insights, and recommend visualizations using any AI API (OpenAI, Azure OpenAI, Anthropic, etc.).
It supports a variety of data formats including:

📊 CSV
📄 Excel
📝 Text Files
📷 Images
📑 PDF
📂 Word Documents
No more complex configurations! Just connect your AI API and start analyzing.

🛠️ Key Features
✅ AI-Powered Insights: Automatically extracts key insights from your data.
✅ Anomaly Detection: Detects unusual patterns using adaptive AI logic.
✅ Visualization Suggestions: AI recommends the best visual charts for your data.
✅ Multi-File Support: Supports one or multiple files across different formats in a single analysis.
✅ Flexible API Integration: Works seamlessly with OpenAI, Azure OpenAI, Anthropic, and more.

📦 Installation
Ensure you have Python 3.7+ installed.

pip install ai-datasense


🚀 Quick Start Guide
1️⃣ Setup Your API Details
Create a Python script (test.py) in your project directory and add the following:

from ai_datasense.core import DataAnalyzer

# Initialize DataAnalyzer with API details
analyzer = DataAnalyzer(
    api_provider="openai",  # or azure_openai, anthropic, etc.
    api_key="your_api_key_here",  # Replace with your actual API key
    api_url="your_api_url_here",
    model="gpt-4o-mini"
)

# List of files to analyze (Uncomment other file types as needed)
file_paths = [
    "test_data.csv",    # CSV file
    # "data.xlsx",       # Excel file
    # "report.pdf",      # PDF file
    # "notes.txt",       # Text file
    # "image.png"        # Image file
]

# Analyze files
results = analyzer.analyze(file_paths)

# Iterate through results
for file, result in results.items():
    print(f"\n📂 **Results for {file}:**")
    
    try:
        # Extract content from AI response
        content = result['choices'][0]['message']['content']
        
        # Parse Key Insights
        if "### Key Insights" in content:
            insights = content.split("### Key Insights")[1].split("###")[0].strip()
            print("\n🧠 **Key Insights:**")
            print(insights)
        else:
            print("\n🧠 **Key Insights:** No insights provided.")
        
        # Parse Anomalies
        if "### Anomalies" in content:
            anomalies = content.split("### Anomalies")[1].split("###")[0].strip()
            print("\n🚨 **Anomalies:**")
            print(anomalies)
        else:
            print("\n🚨 **Anomalies:** No anomalies detected.")
        
        # Parse Visualization Recommendations
        if "### Visualization Recommendations" in content:
            visualizations = content.split("### Visualization Recommendations")[1].strip()
            print("\n📊 **Visualization Recommendations:**")
            print(visualizations)
        else:
            print("\n📊 **Visualization Recommendations:** No visualization suggestions provided.")
    
    except (KeyError, IndexError, AttributeError) as e:
        print(f"\n❌ Error extracting data from {file}: {e}")
2️⃣ Run the Script
Make sure you're in your project directory and your virtual environment is activated:


venv\Scripts\activate  # For Windows
source venv/bin/activate  # For macOS/Linux

# Run the script
python test.py
3️⃣ Expected Output
📂 Results for test_data.csv:
🧠 Key Insights:

Top-performing categories (e.g., Electronics, Home Appliances).
Regional trends and sales behaviors.
🚨 Anomalies:

High sales from low quantities sold.
Discount irregularities impacting sales patterns.
📊 Visualization Recommendations:

Bar charts for category-wise sales.
Scatter plots for discount vs. sales trends.
Line charts for sales over time.
4️⃣ Switch Between AI Providers
You can easily switch to another AI provider by updating the api_provider, api_key, api_url, and model parameters.

### 📂 Test Data File
- `test_data.csv`: A sample dataset included for demonstration and quick testing of the AI DataSense package.
- Users can replace it with their own data files for analysis.


Azure OpenAI Example:
python
Copy code
analyzer = DataAnalyzer(
    api_provider="azure_openai",
    api_key="your_azure_api_key",
    api_url="your_azure_api_endpoint",
    model="gpt-4"
)
Anthropic Example:
python
Copy code
analyzer = DataAnalyzer(
    api_provider="anthropic",
    api_key="your_anthropic_api_key",
    api_url="https://api.anthropic.com/v1/complete",
    model="claude-2"
)


📂 Supported Data Formats
CSV: Spreadsheets with comma-separated values.
Excel: Complex data sheets (.xlsx).
Text Files: Plain text data analysis (.txt).
PDF: Document analysis and text extraction (.pdf).
Word: Document insights (.docx).
Images: Visual data extraction (.png, .jpg).
🧠 API Providers Supported
OpenAI
Azure OpenAI
Anthropic
HuggingFace API
Simply provide your API key, endpoint, and model.

📊 Example Output
🧠 Insights Example:
text
Copy code
Key Insights:
- Electronics dominates sales with high-ticket items.
- South region leads in home appliance sales.
- Discounts on Accessories category increased sales volume.
📊 Visualization Suggestions:
📊 Bar Chart: Sales by Category
📈 Line Chart: Sales Trends Over Time
🌍 Heatmap: Regional Sales Performance
🤝 Contributing
Contributions are welcome!

Fork the repository.
Create a new branch (git checkout -b feature-new-feature).
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature-new-feature).
Open a Pull Request.

📄 License
This project is licensed under the MIT License. 

