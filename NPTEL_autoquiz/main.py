from selenium import webdriver
from selenium.webdriver.common.by import By
import openai
import time

openai.api_key = 'your_openai_api_key_here'

def get_chatgpt_answer(question, options):

    prompt = f"Question: {question}\nOptions:\n" + "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(options)) + "\nAnswer:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return answer


driver = webdriver.Chrome()  # webdriver.Firefox()

driver.get('https://onlinecourses.nptel.ac.in/noc24_bt58/unit?unit=28&assessment=164')

time.sleep(30)

question_elements = driver.find_elements(By.CLASS_NAME, 'gcb-question-row')

for question_element in question_elements:
    question_text = question_element.find_element(By.CLASS_NAME, 'qt-question').text
    print(f"Question: {question_text}")

    option_elements = question_element.find_elements(By.CLASS_NAME, 'gcb-mcq-choice')
    options = [opt.find_element(By.TAG_NAME, 'label').text for opt in option_elements]
    
    print("Options:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    answer = get_chatgpt_answer(question_text, options)
    print(f"Answer from ChatGPT: {answer}")

    for option_element in option_elements:
        option_text = option_element.find_element(By.TAG_NAME, 'label').text
        if answer.lower() in option_text.lower(): 
            option_element.find_element(By.TAG_NAME, 'input').click()
            break

driver.find_element(By.ID, 'submitbutton').click()  

driver.quit()
