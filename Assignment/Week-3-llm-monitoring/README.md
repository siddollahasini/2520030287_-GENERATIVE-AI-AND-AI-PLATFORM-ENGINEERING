Week 3 – LLM Usage Tracking

Aim:
To track the usage details of LLM calls, such as tokens, response time and estimated cost, and save the details in MongoDB.

What I Did:
1.I created a Week 3 project using Python in VS Code.
2.I used main.py to run the program.
3.I used llm_client.py to connect with the LLM.
4.I used usage_logger.py to record the usage details.
5.I configured the required environment variables in the .env file.
6.I used MongoDB to store the usage information.
7.I added timeout and retry handling for API calls.
8.I executed the program using the Ollama provider.

Project Files:
1.main.py – Runs the main program.
2.llm_client.py – Handles the LLM connection.
3.usage_logger.py – Records token usage, latency and cost.
4.test_client.py – Tests the client.
5.requirements.txt – Contains the required packages.
6.env – Stores environment variables.

Command Used
powershell
python main.py

What I Understood:
1.I learned how to track input and output tokens.
2.I understood how to measure response time (latency).
3.I learned how estimated LLM cost is calculated.
4.I understood how to save usage details in MongoDB.
5.I learned why timeouts and retries are useful.

Result:
The program was executed successfully using Ollama.
The usage details were saved to MongoDB.

Conclusion:
Through this experiment, I learned how to monitor LLM usage by tracking tokens, latency and estimated cost. I also understood how to store the usage details in MongoDB and handle retries.