
import google.generativeai as genai
import json
import os


res_list = []

genai.configure(api_key='API_Key')
json_path = 'Mechanics/classification/classification_en.json'
video_prefix = 'Mechanics/classification/'
with open(json_path) as f:
   data = json.load(f)

output_json_list = []   
for data_each in data:
    prompt = data_each['instruction']
    video_file_name = os.path.join(video_prefix, data_each['video_path'])
    
    print(f"Uploading file...")
    video_file = genai.upload_file(path=video_file_name)
    print(f"Completed upload: {video_file.uri}")


    while video_file.state.name == "PROCESSING":
        print('Waiting for video to be processed.')
        video_file = genai.get_file(video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError(video_file.state.name)
    print(f'Video processing complete: ' + video_file.uri)

# Set the model to Gemini 1.5 Pro.
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Make the LLM request.
    print("Making LLM inference request...")
    response = model.generate_content([prompt, video_file],
                                    request_options={"timeout": 600})
    print(response.text)
    data_each['prediction'] = response.text
    output_json_list.append(data_each)
    genai.delete_file(video_file.name)
    print(f'Deleted file {video_file.uri}')   
with open(json_path, 'w', encoding='utf-8') as fw:
    json.dump(output_json_list, fw, ensure_ascii=False, indent=4)
