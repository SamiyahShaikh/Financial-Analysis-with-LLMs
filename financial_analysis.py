from transformers import pipeline

# Load pre-trained LLM model
model = pipeline('text-generation', model="gpt-3")

def generate_report(financial_data):
    """
    Generate a financial analysis report using LLM based on structured data.
    
    :param financial_data: DataFrame containing financial metrics.
    :return: Generated text report.
    """
    prompt = f"Analyze the financial health based on the following metrics: {financial_data.to_dict()}"
    response = model(prompt, max_length=300)
    
    return response[0]['generated_text']

