Week 5 – Token Economics

Aim:
To calculate the token usage, estimated cost and rate limits required for an LLM-based feature.

What I Did:
1.I created a Week 5 project using Python in VS Code.
2.I created budget.py to calculate the token usage and estimated cost.
3.I used input tokens and output tokens per day for the calculations.
4.I calculated the total tokens used per day.
5.I estimated the daily and monthly cost.
6.I checked the RPM and TPM limits.
7.I used unit tests to verify the calculations.

Commands Used:
To install the required packages:

powershell
pip install -r requirements.txt

To run the program:
powershell
python budget.py

To execute the tests:
powershell
python -m unittest -v test_budget.py

What I Understood:
1.I learned what token economics means.
2.I understood how to calculate daily and monthly token usage.
3.I learned how to estimate the cost of using an LLM.
4.I understood RPM (Requests Per Minute) and TPM (Tokens Per Minute).
5.I learned how to check whether a feature fits within the available budget.
6.I understood the importance of unit testing.

Result:
I successfully executed the Token Economics program.The program generated a report showing input tokens, output tokens, total tokens, daily cost, monthly cost, RPM and TPM.The RPM capacity, TPM capacity and daily budget checks passed. The monthly budget showed REVIEW.I also executed the unit tests. All 4 tests passed successfully.

Conclusion
Through this experiment, I learned how to calculate token usage, estimate LLM costs and check rate limits. I also verified the calculations using unit tests.

Conclusion:
Through this experiment, I learned how to estimate the token usage and cost of an LLM feature before building it. I also understood how to check rate limits and verify calculations using unit tests.