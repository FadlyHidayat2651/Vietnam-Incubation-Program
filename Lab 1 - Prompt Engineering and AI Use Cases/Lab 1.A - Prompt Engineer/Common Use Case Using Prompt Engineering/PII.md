## Personally Identifiable Information
In this demonstration, your objective is to effectively obtain **Personal Identifiable Information (PII)** based on the information from the passage text based on your specific requirements. Feel free to use zero-shot, one-shot, or few-shot learning, and adjust your model parameters and instructions from the prompt.

***

### Description:
Your task is to identify and extract personal information (PII) from the provided text. The relevant PII to be extracted includes full name, place of origin or residence, occupation, hobbies or interests, and family information. Please identify and record the relevant PII from the given text.

**Instruction:** Your task is to identify and extract personal information (PII) from the text. Personal information that needs to be extracted includes full name, place of residence or origin, occupation, hobbies or interests, and family information. Please identify and record relevant PII from the text provided. Make sure not to add or subtract from the context provided and ensure answers are PII only.

**Example:**
- On Monday, May 12 2024, I attended a seminar at Hotel XYZ. There, I met a young man named John Doe. John is a software engineer working at a leading technology company. She is originally from New York City and currently lives in a downtown apartment. In addition to being an extremely talented professional, John is also a sports lover, especially basketball. He shared stories about his experience playing basketball on a college team and his excitement when his team achieved victory in the regional tournament. John also mentioned that he has a sister who lives in Los Angeles and that she is the oldest child in the family. He is interested in the topic of AI and plans to attend a Gen AI workshop next month to expand his knowledge in the field.

**Result Example:**
```
Full name: John Doe
Residence: apartment in the city center
Origin: New York City
Occupation: software engineer
Hobbies/interests: basketball
Family information: has a sister living in Los Angeles, the oldest child in her family
```

**Exercise:**
- At a get-together in a city cafe, I met a woman named Emily Smith. Emily is a graphic designer living in a small apartment in the suburbs. He was born in Chicago but moved to San Francisco to pursue a career in design. Emily is a fan of fine art and often spends her free time visiting local art galleries. He is also a big fan of indie music and loves attending concerts on the weekends. Emily said that she has a pet cat named Luna who always accompanies her in her apartment. Additionally, she is an active member in the local designer community and frequently attends meetups and workshops to continually improve her skills in graphic design.

***

### Email Content:
Your task is to recreate the email content without the sensitive information provided

**Instruction:** Based on the email above, do the following: recreate the email by removing sensitive personal information such as individual names, addresses, telephone numbers, cell phone numbers, email addresses, credit card numbers, and medical information. Make sure not to add or subtract from the context of the email provided.

**Example:**
```
Dear. Mr Son,

Hopefully this email finds you in good health. Let me introduce myself, my name is Surya Permana, I am a salesperson at Cheap Dealz Auto, a trusted car dealer in Surabaya.
I know that you have just bought a new car. I would like to congratulate you on your purchase of your new car, and also want to offer a special offer for other new cars.
Currently, Cheap Dealz Auto is holding a big promotion for new cars. We offer a wide range of new cars at very attractive prices.
Apart from that, we also provide various attractive bonuses and prizes for every new car purchase.

If you are interested in finding out more about our promotions, please contact me via the telephone number or email below.
I will be happy to help you choose a new car that suits your needs and budget.

Thank you for your attention sir.

Yours faithfully,

Surya Permana
Cheap Dealz Auto

Jl. Soekarno Hatta No. 125, Surabaya

Mobile no: (0812)12293456
Email: SuryaPermana@CDAuto"
```

**Result Example:**
```
Dear. Father,

Hopefully this email finds you in good health. Let me introduce myself, I am a salesperson at Cheap Dealz Auto, a trusted car dealer in Surabaya.
I know that you have just bought a new car. I would like to congratulate you on your purchase of your new car, and also want to offer a special offer for other new cars.
Currently, Cheap Dealz Auto is holding a big promotion for new cars. We offer a wide range of new cars at very attractive prices.
Apart from that, we also provide various attractive bonuses and prizes for every new car purchase.

If you are interested in finding out more about our promo, please contact me via the contact below.
I will be happy to help you choose a new car that suits your needs and budget.

Thank you for your attention sir.

Yours faithfully,
Cheap Dealz Auto
```


**Exercise:**
```
Dear. Mrs. Anisa,

Hopefully this message finds you in good condition. I, Farhan Ardiansyah, representing the marketing team from Gaya Furniture, would like to convey warm greetings to you.
We would like to thank you for purchasing Mother's new wardrobe some time ago. We hope that this cupboard can fulfill your storage needs well.

To expand our offer, we would like to inform you that Gaya Furniture is currently holding a special promotion for its bedroom furniture collection. We offer various designs of wardrobes, dressing tables and beds at attractive discounts. Apart from that, we also provide a bonus package in the form of a bed lamp and lounge chair for every purchase of a complete bedroom package.

If you are interested in seeing more options or have questions about our promotions, please feel free to contact me via the phone number or email below. We are ready to help you with full attention.

Thank you for your support and trust in Gaya Furniture.

Best regards,

Farhan Ardiansyah
Furniture Style

Jl. General Sudirman No. 78, Jakarta

Tel: (021) 12345678
Email: Farhan@gayafurniture.com
```

***
