               Week-1 LLM

Aim:
To connect Python with Gemini API and get a response from an AI model using a text prompt.

Steps:
1. First, I created a folder named Week1 LLM in VS Code.
2. I created a Python virtual environment for the project.
3. I installed the required libraries.
4. I created a .env file and added my Gemini API key.
5. I created main.py and wrote the Python code to connect with Gemini.
6. In the program, I used a prompt to ask: "What is Artificial Intelligence? Explain in simple words."
7. I used the Gemini API URL to send the request and tried to get the AI response.

 Commands I have Used:
To activate the virtual environment:
powershell
.\.venv\Scripts\Activate.ps1
To run the program:
powershell
python main.py

What I  have Understood:
1. I understood what an LLM is and how it gives answers to our questions.
2. I learned how to use an API key in a Python program.
3. I understood how to send a prompt to Gemini using an API request.
4. I learned how to read the response in JSON format.
5.  I also understood how to handle errors in Python:
 Result:
I successfully loaded my Gemini API key and checked that the model was available.
When I ran main.py and I received a 503 (UNAVAILABLE) error because the Gemini model was experiencing high demand. So, I still need to verify the successful AI response after the service becomes available.

Conclusion:
Through this experiment, I have learned how to connect Python with Gemini API, send a prompt, and try to get a response from an LLM. I also learned how to check and understand API errors.