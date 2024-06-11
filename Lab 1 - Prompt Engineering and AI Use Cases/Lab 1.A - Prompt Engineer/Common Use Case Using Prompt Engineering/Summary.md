## Summary
In this demonstration, your objective is to get a **Summarization** based on the information from the passage text based on your specific requirements. Feel free to use zero-shot, one-shot, or few-shot learning, and adjust your model parameters and instructions from the prompt.


***


### Meeting Summarization:
Your task is to summarize the information from the meeting conversation and generate Minutes Of Meeting (MoM) report.

**Instructions:**
You are the assistant whose job is to analyze conversations in meetings. Make it in Indonesian in Minutes Of Meeting (MoM) format, including the topic, when the meeting will be held, list of participants, summary, important points in list form, and next steps to be taken.


**Example:**
```
00:00 [August] Good morning, everyone. Thank you for attending today's online meeting. I am very happy that the weather today is good because yesterday, May 7, it continued to rain.
00:05 [Agus] We will start by discussing the implementation of a new system for the production process which is the main focus.
00:15 [Agus] Mr Budi, please provide an in-depth explanation regarding the design and architecture of the new system that will be implemented.
00:30 [Budi] Sure. The new system we are planning is designed to leverage advanced cloud computing infrastructure, with enhanced security layers and robust redundancy mechanisms to ensure operational reliability.
00:45 [Budi] The main advantages of this implementation are increased efficiency through elastic use of resources and scalability that can be adapted to production needs, as well as smoother integration with existing systems.
01:05 [Agus] Thank you, Mr Budi, very comprehensive explanation.
01:10 [Agus] Do you have any further questions regarding infrastructure or other technical aspects?
01:15 [Cici] I want to understand more deeply about the strategies that will be implemented in mitigating risks and dealing with potential obstacles during the migration process.
01:30 [Budi] Sure. We have designed a comprehensive risk mitigation plan, including detailed testing, disaster recovery and reverse planning. Apart from that, we also have a response team that is ready to proactively handle any problems that may arise.
01:45 [Agus] Very relevant question, Cici. Thank you for your intelligence in asking this question.
01:50 [Agus] Are there any additional considerations or thoughts before we move on to the next stage?
01:55 [Dedi] I support the implementation of this new system, but I would like to suggest that there be regular evaluations to ensure that the system performance remains optimal and in line with expectations.
02:00 [Agus] I agree with the suggestion. Regular evaluation will be an important part of the continuous development and improvement cycle.
02:05 [Agus] OK, with support from all parties, I think we have enough for the current discussion stage. Thank you for the invaluable contributions and thoughts from each of you.
02:10 [Agus] Mr Budi, I hope you can coordinate with the IT team to start the data migration phase that has been carefully planned.
```


**Result Example:**
```
Minutes of Meeting (MoM)

Topic: Implementation of a New System for Production Processes
Date: May 8
List of participants:
- Agus
- Budi
- Cici
- Dedi

Summary:
This online meeting discussed the implementation of a new system for the production process which was the main focus. Pak Budi explained the design and architecture of the new system that will be implemented, including key benefits such as increased efficiency and smoother integration with existing systems. Participants also discussed risk mitigation strategies and dealing with potential obstacles during the migration process.

Important point:
- Implementation of a new system for the production process
- New system design and architecture using advanced cloud computing infrastructure
- Key benefits: improved efficiency and smoother integration with existing systems
- Risk mitigation strategies and dealing with potential obstacles during the migration process
- Regular evaluation to ensure system performance remains optimal

Next Steps:
- Pak Budi will coordinate with the IT team to start the data migration stage which has been carefully planned.
- Regular evaluations will be carried out to ensure system performance remains optimal and meets expectations.
```

**Exercise:**
```
10:00 [Rina] Good morning, everyone. Thank you for joining today's HR strategic meeting, May 13, 2024. We will start by discussing employee development plans for this year.
10:05 [Rina] First of all, I would like to say that our target this year is to increase employee retention rate by 15% from the previous year.
10:10 [Rina] To achieve this target, we have designed a more structured and comprehensive training and development program.
10:15 [Rina] Mr Joko, could you provide a brief overview of the planned training program?
10:20 [Joko] Sure, Rina. We plan a training program consisting of a series of online courses and in-person training tailored to the needs of employees in each department.
10:25 [Joko] In addition, we will also hold mentoring and coaching sessions to assist employees in developing specific skills and achieving their career goals.
10:30 [Rina] Thank you, Mr Joko, that plan sounds very comprehensive.
10:35 [Rina] Do you have any other questions or suggestions regarding training and development programs?
10:40 [Santi] I would like to suggest that there be a clear evaluation mechanism to measure the effectiveness of the training program. What is the evaluation plan?
10:45 [Joko] We have planned participant satisfaction surveys after each training session, as well as conducting pre- and post-training performance evaluations to measure related performance improvements.
10:50 [Rina] Good consideration, Santi. Evaluation will be key to ensuring our training program runs well.
10:55 [Rina] Any other suggestions or considerations before we move on to the next step?
11:00 [Budi] I would like to suggest that we also consider a reward and incentive program to appreciate employee participation and achievements in this training program.
11:05 [Rina] I agree with that suggestion, Budi. A reward program will be an additional motivation for employees to take an active part in their development.
11:10 [Rina] With support from all parties, I think we are ready to move to the implementation stage. Thank you for the invaluable contributions and ideas from each of you.
11:15 [Rina] Mr Joko, please coordinate with the training team to start implementing the employee development program according to the plan that has been prepared.
```


***


### Meeting Summarization in JSON:
Your task is to summarize the information based on the information provided.

**Instructions:**
You are the assistant whose job is to analyze conversations in meetings. The answer is only in the form of a json format structure which contains a summary of the transcript without adding any other information other than the json format

**Example:**
Inputs:
```
00:00 [Budi] Hello everyone,
00:05 [Budi] I want to share an update about project Y today.
00:15 [Budi] Project Y has entered the development stage. We've completed some key features, and we're working on others.
00:30 [Cici] Very good!
00:35 [Cici] I heard from customer A today, and they are very happy with project Y. They said that this project met all their needs.
00:45 [Dedi] Customer B also said they were very satisfied with project Y. They only had a few minor change requests.
01:05 [Budi] We will work with customer B to fulfill their change request. We hope to complete the development of the Y project on Monday, October 30 2023, at 17.00 WIB.
01:20 [Cici] OK, I will contact customers A and B to arrange a demo meeting on Friday, October 27 2023, at 14.00 WIB.
01:30 [Dedi] I will prepare the Y project system design document to be submitted to the customer on Wednesday, October 25 2023, at 11.00 WIB.
01:40 [Budi] Thank you all for your hard work.
```

Output:
```
{
 "action_items": [
 {
 "action": "Work on other features of project Y.",
 "due_to": "Monday, October 30 2023, 17.00 WIB",
 "pic": "Budi"
 },
 {
 "action": "Answer customer B's question about project Y.",
 "due_to": "Monday, October 30 2023, 17.00 WIB",
 "pic": "Budi and Dedi"
 },
 {
 "action": "Prepare project Y system design documents for delivery to customers.",
 "due_to": "Wednesday, October 25 2023, 11.00 WIB",
 "pic": "Dedi"
 },
 {
 "action": "Contact customers A and B to set up a demo meeting.",
 "due_to": "Friday, October 27 2023, 14.00 WIB",
 "pic": "Cici"
 }
 ]
}
```

**Exercise:**
```
00:00 [Manager] Good morning team, I hope everything is well today.
00:05 [Manager] As discussed previously, we need to review Project Alpha's progress and plan next steps.
00:15 [Project Lead] I am pleased to inform you that Project Alpha has reached the final development stage.
00:25 [Project Lead] Currently, we are testing the integration between modules A and B.
00:35 [Developer 1] There were a few minor issues that came up during testing, but we're in the process of resolving them.
00:45 [Manager] Good. We need to ensure that all bugs are fixed before the advanced testing phase.
00:55 [QA Lead] I will ensure the QA team checks all features and reports bugs as quickly as possible.
01:05 [Project Lead] I hope we can complete additional testing and bug fixes by Wednesday, May 25, 2024, at 18:00 WIB.
01:20 [Manager] OK. After that, we need to plan the beta launch.
01:30 [Marketing Lead] I will coordinate with the marketing team to prepare the beta launch campaign.
01:40 [Manager] Apart from that, we also need to prepare training materials for customers who will use this product.
01:50 [Training Lead] I will lead the training team to prepare training materials and schedules.
02:05 [Manager] Lastly, I would like to convey that the project presentation will be held on Friday, May 26 2024, at 10.00 WIB.
02:15 [Manager] Thank you for your dedication and hard work. Let's make sure Project Alpha is a successful launch!
```

