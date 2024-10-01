import React, { useState } from 'react';

function FinancialAnalysis() {
    const [report, setReport] = useState('');

    const analyzeData = async () => {
        const filePath = document.getElementById('filePath').value;
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ file_path: filePath })
        });
        const data = await response.json();
        setReport(data.report);
    };

    return (
        <div>
            <h1>Financial Analysis & Automation</h1>
            <input id="filePath" type="text" placeholder="Enter data file path" />
            <button onClick={analyzeData}>Analyze</button>
            <p>{report}</p>
        </div>
    );
}

export default FinancialAnalysis;
