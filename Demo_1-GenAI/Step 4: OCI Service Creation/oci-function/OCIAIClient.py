import requests
import json
import re

LLM_ENDPOINT = "http://nim-route.apps.nvidia.openshift.buzz/v1/completions"
headers = {"Content-Type": "application/json"}

class OCIAIClient:

    def get_unique_sentences_large_text(self, text):
        """
        Processes large text input and returns only unique sentences,
        determined by the first 4 words of each sentence.
        """
        # Normalize line breaks and whitespace
        text = re.sub(r'\s+', ' ', text.strip())

        # Split the text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        seen_starts = set()
        unique_sentences = []

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            words = sentence.split()
            if len(words) < 4:
                key = ' '.join(words).lower()
            else:
                key = ' '.join(words[:4]).lower()
            
            if key not in seen_starts:
                seen_starts.add(key)
                unique_sentences.append(sentence)

        return ' '.join(unique_sentences)


    def get_summary(self, text_content):

        final_prompt =(
        "You are a helpful assistant. Your job is to create a paragraph the input text. Please include all information related to root cause and any impact to aircraft equipment\n\n"
        "=== TASK ===\n"
        "Write a detailed paragraph that captures all the key points.\n"
        "Do NOT repeat any phrases. Be concise and informative.\n\n"
        "=== FORMAT ===\n"
        "Paragraph:\n"
        "<Write the paragraph here>\n\n"
        "END\n\n"
        "=== INPUT TEXT ===\n"
        f"{text_content}")

        payload = {
        "model": "meta/llama-3.1-8b-instruct",
        "prompt": final_prompt,
        "max_tokens": 1000,
        "temperature": 0.2,  # Makes it more focused
        "stop": ["\n\n"]     # Optional: helps truncate after a thought
        }

        response = requests.post(LLM_ENDPOINT, headers=headers, data=json.dumps(payload))

        if response.ok:
            result = response.json()
            # Parse and extract generated text
            if "choices" in result and len(result["choices"]) > 0:
                output_text = result["choices"][0]["text"].strip()
                #print("Assistant:", output_text)
                return self.get_unique_sentences_large_text(output_text)
            else:
                print("No text found in response.")
                return ""
        else:
            print("Request failed:", response.status_code)
            print(response.text)
            return ""
        
    llama_prompt = """
    Your task is to write ONLY a title under 100 characters for the content below.

    ✱ Do NOT include any explanations, summaries, or additional text.
    ✱ Do NOT repeat the instructions or say "Here is a title".
    ✱ Only respond with the title itself. Max 100 characters.

    Content:
    [Insert your content here]

    Title:
    """

    def extract_title(self, response: str) -> str:
        # Grab the first line that looks like a valid title and under 100 characters
        lines = response.strip().splitlines()
        for line in lines:
            line = line[:100]
            line = line.strip().strip('"')  # remove extra quotes if any
        return self.extract_before_5_spaces(line)
            #if 5 < len(line) <= 200:
                # return line
        #return "Untitled"    

    def extract_before_5_spaces(self, text):
        """
        Extracts and returns the substring before the first occurrence
        of 5 consecutive spaces.
        """
        split_index = text.find('     ')  # 5 spaces
        if split_index != -1:
            return text[:split_index].strip()
        return text.strip()  # If no 5 spaces found, return the whole string        
        
    def get_title(self, text_content):

        final_prompt = self.llama_prompt.replace("[Insert your content here]", text_content)

        payload = {
        "model": "meta/llama-3.1-8b-instruct",
        #"prompt": "Generate a concise and compelling title (must under 100 characters) for the following content:\n\n" + text_content,
        "prompt" : final_prompt,
        "max_tokens": 1000,
        "temperature": 0.2,  # Makes it more focused
        "stop": ["\n\n"]     # Optional: helps truncate after a thought
        }

        response = requests.post(LLM_ENDPOINT, headers=headers, data=json.dumps(payload))

        if response.ok:
            result = response.json()
            # Parse and extract generated text
            if "choices" in result and len(result["choices"]) > 0:
                output_text = result["choices"][0]["text"].strip()
                #print("Assistant:", output_text)
                return self.extract_title(output_text)
            else:
                print("No text found in response.")
                return ""
        else:
            print("Request failed:", response.status_code)
            print(response.text)
            return ""

# Test
#get_summary("Virginia Beach's summer season brings an influx of visitors, many of whom soak up the sun on the city's 35 miles of coastline. Eco-tourists and anglers come to the area to explore the Hampton Roads Estuary and fish in the Atlantic Ocean. Concerts, festivals, and fireworks displays are regular events during the summer season in Virginia Beach, making it an exciting destination for couples and families alike.")

