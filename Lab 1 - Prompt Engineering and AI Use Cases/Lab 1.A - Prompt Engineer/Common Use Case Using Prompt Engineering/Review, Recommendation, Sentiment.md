## Review, Recommendation, Sentiment
In this demonstration, your objective is to get sentiment **review, recommendation, or sentiment** based on the information from the passage text based on your specific requirements. Feel free to use zero-shot, one-shot, or few-shot learning, and adjust your model parameters and instructions from the prompt.

***

### Product Review:
Your task is to review the information based on the product perspective.


**Instruction:** You are the assistant tasked with analyzing context in product reviews. Find information such as user sentiment (positive/neutral/negative) and why, whether there is context that reflects disappointment or satisfaction, the name of the product reviewed, and provide information about the company in question. As an assistant in product reviews, your job is to analyze and collect relevant information from available reviews. Answer questions in Indonesian and arrange them in JSON format without additional information or responses.


**Example:**
- Coincidentally, I needed a lamp for my bedroom, and it turned out that this LightPro bedroom lamp also had a spare battery, and in terms of price it was also quite affordable, so I decided to buy it straight away. Even though the cable was damaged during shipping, the seller was willing to replace it. And it turned out there were parts that were incomplete too, and I immediately informed the seller. Incomplete items are sent together with a new cable! in my opinion Lumina is a company that cares about its customers, and is responsible with their products!!


**Result Example:**
```
{"sentiment":"positive",",
"product": "LightPro night light",
"company": "Lumina"}
```


**Exercise:**
- I'm looking for earphones that are comfortable and have good sound quality for listening to music on the go. I found a product from SoundWave that had good reviews and was quite affordable too. After I bought it, I realized that the sound quality was amazing, but unfortunately one of the earphones didn't work well after a few days of use. I contacted SoundWave customer service, and they quickly sent me new replacement earphones at no additional charge. Apart from that, they also gave me a bonus discount on my next purchase as compensation for the inconvenience I experienced. I really appreciate SoundWave's quick response and friendly service, so I feel confident recommending their products to my friends.


***


### Recommendations
Your task is to give recommendations and suggestions based on the review


**Instruction:** You are the assistant tasked with analyzing context in product reviews. Provide recommendations to improve the product based on the reviews provided


**Example:**
- I usually order food from Thai Delight restaurant directly and am always satisfied with the quality. However, recently I tried using a food delivery application to order food from the restaurant. Unfortunately, I encountered several problems, such as orders that often arrived late and did not match what I ordered. In fact, I once had difficulty contacting customer service when there was a problem with my order.


**Result Example:**
```
1. Increase order accuracy by ensuring that orders sent are as ordered.
2. Increase order delivery speed to reduce customer waiting time.
3. Improve the quality of customer service by ensuring that customers can easily contact customer service when there are problems with orders.
```


**Exercise:**
- I'm a big fan of coffee, and I usually order it from the local coffee shop around where I live. However, when I tried ordering my favorite coffee via a coffee delivery app, I was very satisfied with the experience. My order arrived on time and the coffee I received was still fresh and high quality. The payment process is very easy and comfortable. I will definitely use this app again to order coffee in the future.

***