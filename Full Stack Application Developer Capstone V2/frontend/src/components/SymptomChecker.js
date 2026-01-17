// frontend/src/components/SymptomChecker.js
import React, { useState } from 'react';
import { analyzeSymptoms } from '../services/api';

const SymptomChecker = () => {
  const [symptoms, setSymptoms] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await analyzeSymptoms(symptoms);
      setResults(response.data);
    } catch (error) {
      console.error('API Error:', error);
    }
    setLoading(false);
  };

  return (
    <div className="symptom-checker">
      <h1>AI Health Symptom Checker</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={symptoms}
          onChange={(e) => setSymptoms(e.target.value)}
          placeholder="Describe your symptoms..."
          rows="4"
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Analyzing...' : 'Get AI Assessment'}
        </button>
      </form>
      {results && <RiskAssessment results={results} />}
    </div>
  );
};

export default SymptomChecker;