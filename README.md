# AI-Job-Market-Trends Project

This project analyzes trends in AI-related job postings to understand key patterns in skills demand, salary distributions, and market shifts across countries, industries, and work types.

📊 Overview

We use a dataset of AI job postings containing variables such as salary, required skills, experience, remote work ratio, education level, industry, and more. The analysis includes:
	
	•	Descriptive Statistics & Visualizations: General distributions of salary, experience, remote types, and top industries hiring AI talent.

	•	Skill Demand Analysis: Word clouds, combination analysis, and cluster analysis using NLP methods to identify skill groupings and high-paying combinations.

	•	Salary Prediction Modeling: Using Random Forest regression to understand key salary drivers and feature importances.

	•	Scenario Simulations: Comparing predicted salaries across different remote work types, education levels, company sizes, and industries.

🔥 Key Insights

	•	Years of experience and company location are the strongest predictors of salary.

	•	Remote work flexibility and higher education levels contribute to modest salary increases.

	•	Python, TensorFlow, and cloud tools (like GCP, Azure) are top skills in high-salary roles. 

	•	Large companies pay more consistently across industries.

📁 Files

	•	notebooks/analysis.ipynb: Full analysis code and visualizations.

	•	data/ai_job_postings.csv: Raw data (not included here).

	•	models/salary_predictor.pkl: Trained Random Forest model.


✨ Future Work

	•	Integrate additional features such as job description text embeddings.

	•	Explore salary prediction with deep learning regression models.

	•	Build interactive dashboards for real-time trend updates.

📚 References

	•	Dataset Source: /kaggle/input/global-ai-job-market-and-salary-trends-2025/ai_job_dataset.csv

	•	Scikit-learn documentation: https://scikit-learn.org

⸻

Feel free to contribute by submitting issues or pull requests!

Author: MengNi (Felicia)