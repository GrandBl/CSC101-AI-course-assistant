Generators use Google's latest generative large language models (LLMs), and prompts that you provide, to generate agent behavior and responses at runtime. The available models are provided by Vertex AI. For example, you put a prompt such as "say hello to the user" or "ask how are you", the generator will able to response you various ways, working similar to the AI chat.

- As you can see in the image that I designed a lot of rectangle, it called page, how is it work? Every pages we have the thing called routes every routes require you to trigger the condition to transit to other pages. For example, To start the coversation you will need to say "hello" this word will trigger the conditions being set in "Start Page" whatever response you set in "Start Page", the agent will response. 
![image](https://github.com/user-attachments/assets/7eaaa741-45de-448a-b722-cf5a7898b813)

- Option Page:
- Generator of option page:
  ![image](https://github.com/user-attachments/assets/25339deb-83c4-49f7-8a28-a24af3af6d59)
  ![image](https://github.com/user-attachments/assets/dbb239a5-6cfa-48a8-8481-d087e41cff7d)

  
In this option page, the user will be asked to enter the word that trigger the options, for example: To transit to summary page, the user simply say anything as long as they include the word "summary", then similarly to other pages.

  ![image](https://github.com/user-attachments/assets/a023b873-928d-4f90-9ed7-4c59129731c2)
  ![image](https://github.com/user-attachments/assets/be663e6a-828a-418c-b37b-2fbd92d7371e)

- Activities Page:

Activities page's generator will ask the user to enter chapter and section they want for generate activities.
![image](https://github.com/user-attachments/assets/faa9df4b-cfce-4625-b012-87475fd1791e)

Data store generator will using RAG to answer chapter and section user input.
  ![image](https://github.com/user-attachments/assets/c589c060-b23f-4ee7-a910-d435bb93232d)
  ![image](https://github.com/user-attachments/assets/a4ab213b-a66b-4153-a1eb-9ab6d41051b2)
  ![image](https://github.com/user-attachments/assets/c826af63-d916-47ec-aa04-1c63cbe12836)

Similarly to other page, except generate syllabus.

-Summary Page:
![image](https://github.com/user-attachments/assets/108e3d94-396d-4179-92c9-401ab42429e0)

- Questions Page:
  ![image](https://github.com/user-attachments/assets/29939e34-469b-4d24-9e2f-fe9183246f34)

- Study Points Page:
![image](https://github.com/user-attachments/assets/f9503575-d571-40e6-a1f1-235f34607a6a)

  - Generate Syllabus you will need to set parameter and questions for the user enter
This page will ask the user enter date start course and end course 
![image](https://github.com/user-attachments/assets/8ca1bf69-83ab-489c-b76b-bace5572cb32)
This page will ask the user enter their name.
![image](https://github.com/user-attachments/assets/658e68f3-1d99-4114-b147-c44da13fedce)
This page will ask the user enter course time.
![image](https://github.com/user-attachments/assets/7902678f-a41a-4182-b3bf-16d28a402fab)
This page will ask the user enter course days.
![image](https://github.com/user-attachments/assets/3ced0bd6-f9ac-4509-839f-f33cdd5b79e5)
This page willa ask the user enter course period.
![image](https://github.com/user-attachments/assets/35ced67b-c50f-4774-a1f6-c222d261eaf1)
This page will ask the user enter quizzes/tests.
![image](https://github.com/user-attachments/assets/fc804acc-a693-4c04-b808-34fcf004b3f0)
Finally, you will need to set all new parameter in Generate Syllabus.
![image](https://github.com/user-attachments/assets/44ae7c1e-98c6-481b-b6ed-a88f4e0bb008)
![image](https://github.com/user-attachments/assets/0d046c6c-ba53-42df-b83d-92bb8913d5f2)

