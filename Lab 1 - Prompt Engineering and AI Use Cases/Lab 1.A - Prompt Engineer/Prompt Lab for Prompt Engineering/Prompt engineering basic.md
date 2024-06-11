# Prompt engineering

### 1.0 LLM Foundations
Before we start exploring the capabilities of watsonx.ai, we first need to know about how Large Language Models (LLM) work, and how we can adjust the model and parameters to change the resulting output. Knowing this can help us to more efficiently use the LLM model.

<img width="1728" alt="image" src="https://media.github.ibm.com/user/446934/files/f30b3142-963d-4296-b710-fe4453429142">


When you open watsonx.ai, this is what you will be shown. The large central text area is called Prompt Lab, or Prompt Builder if you choose more advanced views by clicking the checkbox in the top left. On the right side are the parameters of the model that you can use to select to optimize the model's response to your request or prompt. And at the bottom left, there is a summary of the number of tokens used by your prompt during execution.

### 1.1 Tokens
Each time you enter a prompt, your “input tokens” and “generated tokens” will update. Tokens are an important concept to understand as they constrain the performance of your model plus determine the cost of using models. As you will learn throughout the Labs, tokens are not a 1:1 match with words in natural language, but on average, one token is equal to 4 characters. Before sending your prompt to the model, the prompt's text is tokenized or broken into smaller subsets of characters better understood by a model.

It is important to monitor your token usage to know how much information you are feeding into the model with each prompt, as well as how much text is generated for you. Depending on the model selected in Prompt Builder, you will see a max of 2048 or 4096 tokens. Keep in mind that the more expressive you are with your prompt instructions, the less room the model has to respond back to you.

Every time you prompt, “input tokens” and “generated tokens” will be updated. Tokens are an important concept to understand because they limit the performance of your model and determine the cost of using the model. As you will learn in the Lab, tokens are not 1:1 with the words in a sentence, but on average, one token equals 4 characters. Before sending your command to the model, the command text is Tokenized or broken down into smaller subsets of characters that are easier for the model to understand.

It's important to monitor your token usage to know how much information you're feeding into the model in each command, as well as how much text it's generating for you. Depending on the model selected in Prompt Builder, you will see a max of 2048 or 4096 tokens. Remember that the more expressive you are in giving instructions, the less "room" the model has to respond to you.

### 1.2 Everything is text completion
watsonx.ai is not a chatbot interface, sometimes the prompt results do not provide what is expected, but we can give instructions to the LLM model to do some things in a more appropriate way. For example, what if we ask Watsonx.ai to: List the steps for starting an online business

<img width="390" alt="image" src="https://media.github.ibm.com/user/446934/files/aab3be47-ac97-44ba-bdbe-4a15a8f9418e">


The answer above is not what we expected.

### 1.3 Provide an example as guidance (or Single Shot Prompting)
To get better quality responses, provide examples of the type of response you want. In technical terms, this is called Single Shot Prompting.


<img width="447" alt="image" src="https://media.github.ibm.com/user/446934/files/131e4b38-acc6-4215-8951-c4d0895a0fd7">


**Note:** The following image shows the results from watsonx.ai. The gray text is an example of input that can be provided to the model. The text highlighted in blue is the response from the model.

As you can see, providing one example before giving a command to the LLM is called Single Shot Prompting, but adding more examples to the prompt is also common. Generally, providing more than one example is called “Few Shot Prompting” and is a powerful way to ensure you get specific results.

Use the following text, to try Prompt Builder:

```
Mention the steps to start an online business
1. Choose the product or service you will sell.
2. Do market research.
3. Create a business plan.
4. Obtain necessary permits and certifications.
5. Create a website or online store.
6. Promote your business.
7. Good customer service.

Mention 5 steps to start a big scale culinary business 
```

### 1.4 Include descriptive details
The more detailed the instructions are, the better:
- Contents
- Style
- Length
from the response given

<img width="1728" alt="image" src="https://media.github.ibm.com/user/446934/files/ac6c59ef-dbee-49a7-8b08-1b3a3e7a79a4">


## Model Parameter

### 2.0 Adjusting Model Behavior
The first change we can make is what model (LLM) we use to execute our prompt. This is one of the biggest changes you can make, as certain models are made better for certain tasks. Later exercises in this lab will ask you to change the model you use if you want to answer some of the more challenging questions.

In general, some models perform better with summarization, keywords, and semantics, while others perform better with structured text such as HTML, markdown, or JSON. The best way to find out which model is suitable for your use case is to test it, but it's important to know that the choice of model can make a big difference!

watsonx.ai also provides several parameters to configure how LLM responds to requests. Choosing the correct parameters is often more art than science. Investing time to understand the prompting and then changing the parameters of the model can help generate better responses.

Try experimenting with parameter settings using the following text:

```
Mention the steps to start an online business
1. Choose the product or service you will sell.
2. Do market research.
3. Create a business plan.
4. Obtain necessary permits and certifications.
5. Create a website or online store.
6. Promote your business.
7. Good customer service.

Mention 5 steps to start a big scale culinary business
```

### 2.1 Set the min and max tokens

If you feel the resulting text is too short or long, try adjusting the parameters that control the number of new tokens:
- The __Min new tokens__ parameter controls the minimum number of tokens (~words) of the generated response
- The __Max new tokens__ parameter controls the maximum number of tokens (~words) of the generated response

<img width="1728" alt="Screenshot 2024-06-05 at 20 37 45" src="https://media.github.ibm.com/user/446934/files/01db9096-5496-49e6-8307-34654edc8691">


### 2.2 Specify stop sequences

If you specify a _stop sequence_, the output will automatically stop when one of the _stop sequences_ appears in the resulting output.
__double enter__ is usually added to prevent the model from regenerating the output because the number of tokens generated has not reached _max tokens_


### 2.3 Adjust decoding parameters

If the response is too general or distorted, consider adjusting the decoding parameters. Or when the response may be less creative, it is also a good idea to make adjustments.

`Decoding is the process of determining the output sequence based on the input sequence`

- `Greedy decoding` selects the word with the highest probability at each step of the decoding process.
- `Sampling decoding` selects words from a probability distribution at each step
- `Temperature` refers to selecting words with high or low probability. Higher temperature values ​​cause more variability.
- Top-p (core sampling) refers to selecting the smallest set of words whose cumulative probability exceeds p.
- Top-k refers to selecting the k-words with the highest probability at each step. Higher values ​​cause more variability.
The advantage of Greedy decosing is that you will see reproducible results. This can be useful when testing. Setting temperature=0 in the sampling decoding approach gives the same variation as Greedy decoding.

<img width="1728" alt="Screenshot 2024-06-05 at 20 41 37" src="https://media.github.ibm.com/user/446934/files/082f0005-1dbe-4fb4-be89-5305a9302688">

### 2.4 Add a repetition penalty

Sometimes, you will see text that is repeated over and over again. Raising the temperature can sometimes solve the problem. However, when the text still repeats itself even with a higher temperature setting, you can try adding repetition penality. The higher the penalty value, the smaller the possibility of repeated text.


### 2.5 Excellent 3rd party blog post on model parameters

The description above provides a fairly good introduction to what parameters the model has. But you have to read [artikel ini](https://txt.cohere.com/llm-parameters-best-outputs-language-ai) about the parameters that the model has as it can provide excellent additional examples of how the model parameters work plus there are illustrations that can help you better understand the concept. The better you understand the model parameters, the more frustration you will avoid and the easier it will be to adjust the model to work according to your needs.


# General advice

### 3.1 Try different models

If your prompt doesn't produce what you want, especially if the prompt is written in Indonesian, try changing the model option used

<img width="1728" alt="image" src="https://media.github.ibm.com/user/446934/files/7cc5cab0-3da8-4489-bc16-6c2c628c6c05">



### 3.2 Check your use case

LLM has great potential, but LLM lacks logic, knowledge and domain expertise. Some cases are better suited than others: LLM excels at tasks involving _text generation_ or recognizing similar patterns and transforming given text input.

If the _prompt_ given already uses the _best practice_ discussed here, but still does not get good results from any model, it is possible that the case chosen is something that cannot be handled well by LLM.

For example, although we can get pretty decent results for simple arithmetic, LLMs generally don't do math very well:[Researchers find that large language models struggle with math](https://venturebeat.com/business/researchers-find-that-large-language-models-struggle-with-math/)

### 4.0 Balancing intelligence and security

With great artificial intelligence comes higher security risks. Solutions like ChatGPT are Very large Language Models (VLLM) with 175 billion parameters. They were created by the OpenAI team using additional non-public Chat datasets and the Reinforcement Learning Human Feedback (RLHF) dataset. ChatGPT is an LLM built like a chatbot.

At watsonx.ai, we interact directly with smaller LLMs (3-20 billion parameters). This is a wise choice from a security perspective. _prompt injection_ is a big risk for the use of LLM in companies. By using _prompt injection_ , hackers will create complex commands that cause LLMs such as ChatGPT to ignore/bypass security protocols and reveal sensitive company information. Just imagine you are a hacker. Which model would you choose as the target for _prompt injection_? OpenAI's ChatGPT with 175 billion parameters capable of performing thousands of tasks or a smaller, more focused 3 billion parameter model highly customized for a few isolated tasks? Which one has a wider attack surface for prompt re-engineering to occur?

The smaller, simpler model at watsonx.ai is more challenging for would-be hackers. Using many small models rather than one large model like ChatGPT creates a wider distribution of _sensitive entry points_. Each small language model is much more difficult to manipulate because of its limited functionality and the high level of engineering required to perform its main tasks. They do not have various functions like ChatGPT. As programmers know, losing all your resources with just one failure is unwise. It's much better to decompose your solution for security, scalability, and control.

For safety, smaller is better. In addition to the security benefits, there are computational improvements from using smaller, lighter weight models. Let's interact more with LLM watsonx.ai to better understand and learn how to make them respond according to our needs.

### Further Reading
- [OpenAI prompt intro](https://platform.openai.com/docs/guides/gpt-best-practices)
- [OpenAI prompt engineering tutorial](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
- [co:here prompt engineering tutorial](https://docs.cohere.ai/docs/prompt-engineering)
