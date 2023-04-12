# Python Function Templates
> Here are some of the bootsrapped functions that I regularly use

You aren’t meant to master a Programming Language in the beginning.
You’re meant to go build them 

You don’t master a programming concept, 
you apply them in numerous project.
then you continuously improve on them

## Contents

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

## Reference:

https://www.geeksforgeeks.org/optimization-tips-python-code/?ref=rp
