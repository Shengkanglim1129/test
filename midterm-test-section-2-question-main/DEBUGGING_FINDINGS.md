# DEBUGGING_FINDINGS.md

## Bug #1: Application crashes when API key is missing

**Error/Issue Observed:**
App crashed with a traceback when GOOGLE_API_KEY was not set.

**LLM Assistance Used:**
Asked Copilot to identify the cause and suggest a fallback or error message.

**Root Cause:**
The code attempted to initialize ChatGoogleGenerativeAI even if the API key was missing.

**Fix Applied:**
Added .env file with API key. Updated code to check for API key and exit gracefully if missing.

**Verification:**
App now starts and shows a message if the API key is missing.

---

## Bug #2: Environment variables not loaded in main.py and demo.py

**Error/Issue Observed:**
GOOGLE_API_KEY was not recognized even after setting .env.

**LLM Assistance Used:**
Asked Copilot to review code for missing environment variable loading.

**Root Cause:**
`load_dotenv()` was not called in main.py and demo.py.

**Fix Applied:**
Added `from dotenv import load_dotenv; load_dotenv()` at the start of both scripts.

**Verification:**
API key is now loaded and used by the application.

---

## Bug #3: demo.py only initializes FakeNewsSearchTool and passes wrong arguments to ConversationRouter

**Error/Issue Observed:**
Weather and calculator queries did not work in demo.py.

**LLM Assistance Used:**
Asked Copilot to review tool initialization and router arguments.

**Root Cause:**
Only FakeNewsSearchTool was initialized and passed to ConversationRouter.

**Fix Applied:**
Initialized all three tools and passed them to ConversationRouter.

**Verification:**
All demo queries now work as expected.

---

## Bug #4: Calculator tool returns wrong result (adds 1 to result)

**Error/Issue Observed:**
Calculator returned result + 1 for all expressions.

**LLM Assistance Used:**
Asked Copilot to review the calculator tool implementation.

**Root Cause:**
`eval(expression) + 1` was used instead of just `eval(expression)`.

**Fix Applied:**
Removed `+ 1` from the result calculation in FakeCalculatorTool.

**Verification:**
Calculator now returns correct results.

---

## Bug #5: Undefined run_mock_demo() in demo.py

**Error/Issue Observed:**
App crashed with NameError if API key was missing in demo.py.

**LLM Assistance Used:**
Asked Copilot to review fallback logic in demo.py.

**Root Cause:**
`run_mock_demo()` was called but not defined.

**Fix Applied:**
Removed the call and replaced it with a clear message and graceful exit.

**Verification:**
App now exits gracefully if API key is missing.
