# Code Templates for 'Agents in Action' challenge
התבנית הזו באה לחסוך לך להעתיק את הבסיס מהדוקומנטציה הרשמית:) עכשיו הכל מוכן, אין תירוצים...

### מה את צריכה לעשות עכשיו?
1. להוריד אליך מקומית ( או לבצע Fork אם יותר נוח לך) ולהתקין תלויות.
3. ליצור API_KEY בשתי דקות בחינם כאן: https://console.groq.com/keys (אם יש לך מפתח של ספק אחר העזרי בgpt להתאים את הקוד. זה שינוי קטן מאוד).
4. לממש את הקוד ולשתף אותנו בתוצאות.

## תזכורת מושגים (הגדרות מהירות ולא-מקצועיות):
- system prompt - הנחיה כללית שמבהירה לLLM מהו תפקידו הנוכחי ומה מצופה ממנו באופן כללי.
- user prompt - בקשה ספציפית מהLLM
- agent - LLM שמסוגל לפעול עצמאית, להריץ כלים ולעבוד בשלבים מורכבים.
- tool - פונקציה עם תיאור שהagent יכול להריץ


1. create venv - python -m venv venv
2. activate venv - \venv\Scripts\activate
3. install dependecies :
*pip install langchain
*pip install langchain_community.utilities
*pip install langchain-community
*pip install -U langchain-groq   
*pip install wikipedia   
4. create requirement file -   pip freeze > requirements.txt - next time u can use it to install all dependecies
5. Run   pip freeze > requirements.txt

