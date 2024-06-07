# Python Function Templates
> Here are some of the bootsrapped functions that I regularly use

You aren’t meant to master a Programming Language in the beginning.
You’re meant to go build them 

You don’t master a programming concept, 
you apply them in numerous project.
then you continuously improve on them

## Contents

- algorithms - python functions that uses algorithms
- file - python functions that deals in file systems
- rest - python functions that deals with rest apis
- sql - python functions that interacts with sql
- util - python functions as generalized utility 

## Coding Philosophies

### Keep it DRY
"Don't Repeat Your Self"

### S.O.L.I.D. Principles
```
S – Single Responsibility Principle
O – Open-Closed Principle
L – Liskov Substitution Principle
I – Interface Segregation Principle
D – Dependency Inversion Principle
```

### Clean Coding 
> use name revealing variables and functions.  

bad example
```js
import { sub } from './yt';

function run(unit){
  const p = unit.partList[42]
  p.sub.lsn((w) => {
    if (w === 'banana' ){
      sub(unit)
    }
  })
}
```

Good Example
```js
import { forceToSubscribe } from './youtube';

const BRAIN_INDEX = 42;
const TRIGGER_WORD = 'banana';

function brainwashToSubscribeOnTriggerWord(viewer){
  const brain = viewer.organs[TRIGGER_WORD];

  brain.subconscious.listenForWord((word) => {
    if (word === TRIGGER_WORD) {
      forceToSubscribe(viewer)
    }
  })
}
```

## Python Style Guides

- https://peps.python.org/pep-0008/
- https://google.github.io/styleguide/pyguide.html

### Best Practices for Naming Files in Python

1. **Use lowercase letters and underscores (`snake_case`)**:
   - **Example**: `my_script.py`, `data_processing.py`
   - **Reason**: Using lowercase letters and underscores (snake_case) is consistent with PEP 8, the Python Enhancement Proposal that outlines conventions for writing readable code. This style improves readability and consistency.

2. **Be descriptive and concise**:
   - **Example**: `data_loader.py` instead of `dl.py`
   - **Reason**: Descriptive names make it clear what the file's purpose is, which helps other developers (and your future self) understand the project structure and find files quickly.

3. **Avoid using reserved keywords and built-in names**:
   - **Example**: Avoid names like `list.py`, `test.py`
   - **Reason**: Using reserved keywords or names of built-in modules can cause conflicts and unexpected behaviors in your code.

4. **Use hyphens only if necessary** (and prefer underscores):
   - **Example**: `my_script.py` instead of `my-script.py`
   - **Reason**: While some filesystems allow hyphens, underscores are more common in Python code and are recommended by PEP 8. Hyphens can also cause issues if used in module names since they are not valid characters in Python identifiers.

5. **Reflect the content or functionality of the file**:
   - **Example**: `user_authentication.py` for a file handling user authentication logic
   - **Reason**: Clear, content-specific names help quickly identify the purpose of the file without needing to open and read through the code.

6. **Avoid excessively long names**:
   - **Example**: `process_data.py` instead of `data_processing_for_experiments.py`
   - **Reason**: While being descriptive is important, excessively long names can be cumbersome to type and manage. Aim for a balance between descriptiveness and brevity.

7. **Use consistent naming conventions throughout the project**:
   - **Example**: If you use `snake_case` for one file, use it for all files.
   - **Reason**: Consistency across your project makes it easier to navigate and reduces cognitive load when switching between different parts of the project.

### Summary

Following these best practices for naming files in Python can lead to a more organized, readable, and maintainable codebase. Consistent and descriptive naming conventions help developers quickly understand the structure and purpose of files within a project, making collaboration and future development smoother.

## Rush 

go to ./freelance.md 

scan image text 
https://github.com/tesseract-ocr/tesseract

## TO DO 
- Image to Video 
https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/?ref=rp

- Discord Bot: 
https://www.geeksforgeeks.org/building-a-discord-bot-in-python/?ref=rp

- Telegram bot
https://www.geeksforgeeks.org/create-a-telegram-bot-using-python/?ref=rp

- Whatsapp bot 
https://www.geeksforgeeks.org/building-whatsapp-bot-on-python/?ref=rp

- Dino Bot Game
https://www.geeksforgeeks.org/google-chrome-dino-bot-using-image-recognition-python/?ref=rp

- Chatter Bot 
https://www.geeksforgeeks.org/chat-bot-in-python-with-chatterbot-module/?ref=rp 

- Reddit Scraper 
https://www.geeksforgeeks.org/scraping-reddit-using-python/?ref=rp 


- Flask Auto doc 
https://www.geeksforgeeks.org/documenting-flask-endpoint-using-flask-autodoc/?ref=rp 

## Cool Projects 

- Face Detection OpenCv  using Webcam
https://www.geeksforgeeks.org/face-detection-using-python-and-opencv-with-webcam/?ref=lbp

- Face and hand landmarks 
https://www.geeksforgeeks.org/face-and-hand-landmarks-detection-using-python-mediapipe-opencv/?ref=rp 

- Filter Colors
https://www.geeksforgeeks.org/filter-color-with-opencv/?ref=lbp

- Face Mask Detection with Python 
https://data-flair.training/blogs/face-mask-detection-with-python/


### Voice Assistant 

https://www.geeksforgeeks.org/junk-file-organizer-python/?ref=lbp
https://www.geeksforgeeks.org/python-create-a-simple-assistant-using-wolfram-alpha-api/?ref=lbp
https://www.geeksforgeeks.org/build-a-virtual-assistant-using-python/
https://www.geeksforgeeks.org/voice-assistant-using-python/?ref=lbp
https://www.geeksforgeeks.org/personal-voice-assistant-in-python/?ref=lbp

## Decorators
```py
def my_decorator(func):
  def wrapper():
    print("Print before function")
    func()
    print("Print after function")
  return wrapper

@my_decorator
def say_hello():
  print("Hello There!")

say_hello()
```
output
```
Print before function
Hello There!
Print after function
```

## Reference:

https://www.geeksforgeeks.org/optimization-tips-python-code/?ref=rp
